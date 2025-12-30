#!/usr/bin/python3
"""
Simple RESTful API using http.server
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_text(self, text, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(text.encode("utf-8"))

    def _send_json(self, data, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        if self.path == "/":
            self._send_text("Hello, this is a simple API!")

        elif self.path == "/data":
            self._send_json({
                "name": "John",
                "age": 30,
                "city": "New York"
            })

        elif self.path == "/status":
            self._send_text("OK")

        elif self.path == "/info":
            self._send_json({
                "version": "1.0",
                "description": "A simple API built with http.server"
            })

        else:
            self._send_text("Endpoint not found", status_code=404)


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()

