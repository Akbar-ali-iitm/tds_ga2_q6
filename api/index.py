from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Absolute path to JSON file
            json_path = os.path.join(os.path.dirname(__file__), "..", "q-vercel-python.json")
            with open(json_path, "r") as f:
                student_data = json.load(f)

            # Parse query ?name=X&name=Y
            parsed = urlparse(self.path)
            query = parse_qs(parsed.query)
            names = query.get("name", [])

            # Extract marks (None if name not found)
            marks = [entry["marks"] for entry in student_data if entry["name"] in names]

            # Response headers
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(json.dumps({"marks": marks}).encode())

        except Exception as e:
            # Log and return error
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": str(e)}
            self.wfile.write(json.dumps(error_message).encode())
