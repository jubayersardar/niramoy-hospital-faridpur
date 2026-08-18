import http.server
import socketserver
import os
import sys
import mimetypes
import urllib.parse

DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Ensure correct MIME types on Windows
mimetypes.init()
mimetypes.add_type('text/html', '.html')
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('image/jpeg', '.jpg')
mimetypes.add_type('image/jpeg', '.jpeg')
mimetypes.add_type('image/png', '.png')
mimetypes.add_type('image/webp', '.webp')
mimetypes.add_type('image/svg+xml', '.svg')
mimetypes.add_type('font/woff2', '.woff2')
mimetypes.add_type('font/woff', '.woff')

class CleanUrlHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.handle_request(send_body=False)

    def do_GET(self):
        self.handle_request(send_body=True)

    def handle_request(self, send_body=True):
        parsed = urllib.parse.urlparse(self.path)
        raw_path = urllib.parse.unquote(parsed.path)
        
        # Normalize path
        clean_path = raw_path.strip('/')
        
        # 1. Root -> index.html
        if not clean_path:
            file_path = os.path.join(DIRECTORY, 'index.html')
        else:
            file_path = os.path.join(DIRECTORY, *clean_path.split('/'))

        # 2. Check if direct file exists
        if os.path.isfile(file_path):
            target_file = file_path
        # 3. Check if clean URL (.html counterpart) exists (e.g., /about -> about.html, /doctors -> doctors.html)
        elif os.path.isfile(file_path + '.html'):
            target_file = file_path + '.html'
        # 4. Check if directory has index.html
        elif os.path.isdir(file_path) and os.path.isfile(os.path.join(file_path, 'index.html')):
            target_file = os.path.join(file_path, 'index.html')
        # 5. Special case: /doctors/ when doctors.html exists in root
        elif clean_path == 'doctors' and os.path.isfile(os.path.join(DIRECTORY, 'doctors.html')):
            target_file = os.path.join(DIRECTORY, 'doctors.html')
        else:
            self.send_error(404, f"File not found: {raw_path}")
            return

        try:
            with open(target_file, 'rb') as f:
                content = f.read()
                
            ctype, _ = mimetypes.guess_type(target_file)
            if not ctype:
                ctype = 'application/octet-stream'
                
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
            self.end_headers()
            
            if send_body:
                self.wfile.write(content)
        except Exception as e:
            self.send_error(500, f"Internal server error: {e}")

    def log_message(self, format, *args):
        # Concise logging
        sys.stderr.write(f"[{self.log_date_time_string()}] {self.address_string()} - {format % args}\n")

class ReusableThreadingServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

def run_server(port=8000):
    try:
        httpd = ReusableThreadingServer(('0.0.0.0', port), CleanUrlHandler)
        print(f"==================================================")
        print(f"  NIRAMAYA Hospital Clean URL Server LIVE")
        print(f"  Listening on: http://localhost:{port}/")
        print(f"  Root Directory: {DIRECTORY}")
        print(f"==================================================")
        httpd.serve_forever()
    except Exception as e:
        print(f"Error starting server on port {port}: {e}")
        sys.exit(1)

if __name__ == '__main__':
    run_server()
