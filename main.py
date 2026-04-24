import os
import threading
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8765
DIR  = os.path.dirname(os.path.abspath(__file__))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def log_message(self, fmt, *args):
        pass  # suppress request noise


def open_browser():
    webbrowser.open(f"http://localhost:{PORT}/index.html")


if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), Handler)
    print(f"Serving ME Planner at http://localhost:{PORT}/index.html")
    print("Press Ctrl+C to stop.")
    threading.Timer(0.5, open_browser).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
