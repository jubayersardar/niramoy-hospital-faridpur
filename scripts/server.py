import http.server
import socketserver
import os
import sys

DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def translate_path(self, path):
        # Strip query string and fragment
        path = path.split('?', 1)[0].split('#', 1)[0]
        words = [w for w in path.split('/') if w]
        path_joined = os.path.join(DIRECTORY, *words) if words else DIRECTORY
        
        # 1. Root or trailing slash request
        if path.endswith('/') or not words:
            idx = os.path.join(path_joined, 'index.html')
            if os.path.isfile(idx):
                return idx
            return path_joined
            
        # 2. Existing static file (.css, .js, .jpg, .png, etc.)
        if os.path.isfile(path_joined):
            return path_joined
            
        # 3. Clean URL route -> check if corresponding .html exists (e.g. /doctors -> doctors.html)
        if os.path.isfile(path_joined + '.html'):
            return path_joined + '.html'
            
        # 4. Directory check with index.html fallback
        if os.path.isdir(path_joined):
            idx = os.path.join(path_joined, 'index.html')
            if os.path.isfile(idx):
                return idx
            return path_joined
            
        return path_joined

    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {self.address_string()} - {format % args}\n")

def run_server(ports=[8000, 8080, 3000]):
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    for port in ports:
        try:
            httpd = socketserver.ThreadingTCPServer(('127.0.0.1', port), CleanUrlHandler)
            print(f"=== NIRAMAYA Hospital Clean URL Server ===")
            print(f"URL: http://localhost:{port}/")
            print(f"Serving from: {DIRECTORY}")
            httpd.serve_forever()
            break
        except OSError:
            continue

if __name__ == '__main__':
    run_server()
