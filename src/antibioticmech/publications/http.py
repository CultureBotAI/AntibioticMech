"""Small retrying HTTP transport with an injectable test seam."""

from __future__ import annotations

import time
import urllib.error
import urllib.parse
import urllib.request
from collections.abc import Callable, Mapping, Sequence
from typing import Protocol

from .models import PublicationSearchError


class Transport(Protocol):
    def get(
        self,
        url: str,
        *,
        params: Mapping[str, str | int] | Sequence[tuple[str, str | int]],
        headers: Mapping[str, str] | None = None,
    ) -> bytes: ...


class UrllibTransport:
    """GET JSON/XML API responses and retry transient provider failures."""

    def __init__(
        self,
        *,
        timeout: float = 60,
        retries: int = 3,
        backoff: float = 1,
        sleeper: Callable[[float], None] = time.sleep,
    ) -> None:
        if retries < 0:
            raise ValueError("retries must be non-negative")
        self.timeout = timeout
        self.retries = retries
        self.backoff = backoff
        self.sleeper = sleeper

    def get(
        self,
        url: str,
        *,
        params: Mapping[str, str | int] | Sequence[tuple[str, str | int]],
        headers: Mapping[str, str] | None = None,
    ) -> bytes:
        query = urllib.parse.urlencode(params)
        request = urllib.request.Request(
            f"{url}?{query}",
            headers={"User-Agent": "AntibioticMech/0.1", **dict(headers or {})},
        )
        for attempt in range(self.retries + 1):
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:  # noqa: S310
                    return response.read()
            except urllib.error.HTTPError as error:
                retryable = error.code == 429 or 500 <= error.code < 600
                if not retryable or attempt == self.retries:
                    detail = error.read(400).decode("utf-8", errors="replace").strip()
                    suffix = f": {detail}" if detail else ""
                    raise PublicationSearchError(
                        f"publication API returned HTTP {error.code}{suffix}"
                    ) from error
                retry_after = error.headers.get("Retry-After")
                delay = float(retry_after) if retry_after and retry_after.isdigit() else 0
                self.sleeper(max(delay, self.backoff * (2**attempt)))
            except urllib.error.URLError as error:
                if attempt == self.retries:
                    raise PublicationSearchError(
                        f"publication API connection failed: {error.reason}"
                    ) from error
                self.sleeper(self.backoff * (2**attempt))
        raise AssertionError("unreachable retry loop")
