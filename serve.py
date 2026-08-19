"""
Niramoy Hospital Faridpur — local dev server with friendly URL routing.

Fixes the gaps in Python's built-in http.server:
  /about             -> /about.html
  /about/            -> /about.html
  /doctors           -> /doctors.html   (the listing page, not the profile folder)
  /doctors/          -> /doctors.html
  /doctors/dr-foo    -> /doctors/dr-foo.html  (per-doctor profile)
  /css/style.css?v=3 -> served as-is (query string stripped for disk lookup)

Usage:
  python serve.py [port]
  default port: 8000
"""
from __future__ import annotations

import os
import sys
import posixpath
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler


# Paths that should NOT be served from a same-named subdirectory.
# /doctors  -> doctors.html (listing page), not /doctors/index.html
FORCE_HTML_ROUTES = {
    "/doctors": "doctors.html",
}


class NiramoyHandler(SimpleHTTPRequestHandler):
    """Static handler that auto-appends .html and routes /doctors/ to the listing page."""

    # Quieter logs
    def log_message(self, fmt: str, *args) -> None:  # noqa: D401
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))

    def translate_path(self, clean_path: str) -> str:  # type: ignore[override]
        """Map an already-cleaned URL path to a disk path.

        Mirrors SimpleHTTPRequestHandler.translate_path but applies our
        FORCE_HTML_ROUTES and .html fallback before hitting the filesystem.
        """
        # Strip query string and fragment if parent didn't already.
        if "?" in clean_path:
            clean_path = clean_path.split("?", 1)[0]
        if "#" in clean_path:
            clean_path = clean_path.split("#", 1)[0]

        # 1) explicit overrides first (e.g. /doctors -> doctors.html)
        # Normalize trailing slash so /doctors and /doctors/ both match.
        normalized = clean_path.rstrip("/") or "/"
        if normalized in FORCE_HTML_ROUTES:
            return os.path.join(os.getcwd(), FORCE_HTML_ROUTES[normalized])

        # 2) default: use the parent behaviour, then try a few fallbacks
        # Strip query string if any slipped through.
        disk = super().translate_path(clean_path)

        if os.path.exists(disk):
            return disk

        # Directory path ending with "/" -> try <dir>/index.html, then <dir>.html
        if clean_path.endswith("/"):
            idx = os.path.join(disk, "index.html")
            if os.path.exists(idx):
                return idx
            # /something/  ->  something.html  (treat as friendly URL for a page)
            sibling = disk.rstrip(os.sep) + ".html"
            if os.path.exists(sibling):
                return sibling
            return disk  # fall through to 404

        # No extension: try appending .html
        if not os.path.splitext(disk)[1]:
            html_try = disk + ".html"
            if os.path.exists(html_try):
                return html_try

        return disk

    def do_GET(self) -> None:  # noqa: N802
        # Strip query string for routing, preserve for client-side cache busting
        parsed = urllib.parse.urlsplit(self.path)
        clean = urllib.parse.unquote(parsed.path)

        # If clean is empty -> /
        if not clean:
            clean = "/"

        # Delegate to the default handler — translate_path will resolve fallbacks
        self.path = parsed.path + (("?" + parsed.query) if parsed.query else "")
        return super().do_GET()


def main() -> None:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)
    print(f"[serve.py] CWD: {root}")
    print(f"[serve.py] Listening on http://127.0.0.1:{port}/")
    print(f"[serve.py] Routes: /about -> about.html, /doctors -> doctors.html, /doctors/dr-foo -> doctors/dr-foo.html")
    httpd = HTTPServer(("127.0.0.1", port), NiramoyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[serve.py] shutting down")
        httpd.server_close()


if __name__ == "__main__":
    main()
