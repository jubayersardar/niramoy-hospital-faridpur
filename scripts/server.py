import http.server
import socketserver
import os
import urllib.parse

PORT = 8000
DIRECTORY = os.path.abspath(os.path.dirname(__file__) + '/..')

class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Parse query string and path
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        query = parsed_url.query

        # If requesting root or directory
        local_path = os.path.join(DIRECTORY, path.lstrip('/'))
        
        # If path doesn't exist directly but path.html does, rewrite internally
        if not os.path.exists(local_path) and not path.endswith('/'):
            html_candidate = local_path + '.html'
            if os.path.exists(html_candidate):
                self.path = path + '.html' + (('?' + query) if query else '')
        
        return super().do_GET()

if __name__ == '__main__':
    # Allow address reuse
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CleanUrlHandler) as httpd:
        print(f"Clean URL Server running at http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
