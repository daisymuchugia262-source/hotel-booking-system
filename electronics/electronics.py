"""Run the PinkVolt storefront locally: python electronics.py"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import webbrowser


if __name__ == "__main__":
    directory = Path(__file__).parent
    class NoCacheHandler(SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
            super().end_headers()

    handler = lambda *args, **kwargs: NoCacheHandler(*args, directory=str(directory), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", 8000), handler)
    print("PinkVolt is running at http://127.0.0.1:8000")
    webbrowser.open("http://127.0.0.1:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
