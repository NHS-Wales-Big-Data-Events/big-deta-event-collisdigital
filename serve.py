#!/usr/bin/env python3
"""Serve the docs/ folder on http://localhost:8000"""
import http.server
import os

PORT = 8000
DIRECTORY = os.path.join(os.path.dirname(__file__), "docs")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


print(f"Serving docs/ at http://localhost:{PORT}")
print("Press Ctrl+C to stop.\n")
with http.server.HTTPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
