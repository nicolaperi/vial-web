#!/usr/bin/env python3

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class CrossOriginIsolatedHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Resource-Policy", "same-origin")
        super().end_headers()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Serve the Vial Web build with COOP/COEP headers."
    )
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument(
        "--dir",
        default=str(Path(__file__).parent / "src" / "build"),
        help="Directory to serve (default: src/build)",
    )
    args = parser.parse_args()

    directory = Path(args.dir).resolve()
    if not directory.exists():
        raise SystemExit(f"Directory not found: {directory}")

    handler = partial(CrossOriginIsolatedHandler, directory=str(directory))
    server = ThreadingHTTPServer(("", args.port), handler)
    print(f"Serving {directory} at http://localhost:{args.port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
