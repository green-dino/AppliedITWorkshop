import http.server
import socketserver
import logging
import signal
import os

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Custom path handling
        if self.path == '':
            self.path = 'index.html'
        elif self.path.startswith('/api/'):
            # Handle API routes if needed
            self.path = 'api' + self.path[4:]
        else:
            # Add a custom 404 error handling
            self.path = '404.html' if not os.path.isfile(self.path[1:]) else self.path

        try:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        except Exception as e:
            logger.error(f"Error processing GET request: {e}")
            self.send_error(500, "Internal Server Error")
            
def handle_exit_signal(signum, frame):
    """Handle exit signals gracefully."""
    logger.info("Shutting down server...")
    httpd.shutdown()
    httpd.server_close()

if __name__ == "__main__":
    # Set up signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, handle_exit_signal)
    signal.signal(signal.SIGTERM, handle_exit_signal)

    handler_object = MyHttpRequestHandler

    while True:
        try:
            with socketserver.TCPServer(("", PORT), handler_object) as httpd:
                logger.info(f"Serving on port {PORT}")
                try:
                    httpd.serve_forever()
                except KeyboardInterrupt:
                    pass  # Allow the server to be stopped cleanly
            break  # Exit loop if successful
        except OSError as e:
            if e.errno == 48:
                logger.warning(f"Port {PORT} is in use. Trying next port.")
                PORT += 1  # Increment port number and try again
            else:
                logger.error(f"Failed to bind server: {e}")
                break
