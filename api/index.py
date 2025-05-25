from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Load JSON file
            json_path = os.path.join(os.path.dirname(__file__), "..", "q-vercel-python.json")
            with open(json_path, "r") as f:
                student_list = json.load(f)

            # Convert list to dict for fast lookup
            student_data = {entry["name"]: entry["marks"] for entry in student_list}

            # Parse query ?name=X&name=Y
            parsed = urlparse(self.path)
            query = parse_qs(parsed.query)
            names = query.get("name", [])

            # Get marks in order (return None if not found)
            marks = [student_data.get(name, None) for name in names]

            # Response
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"marks": marks}).encode())

        except Exception as e:
            # On error, return 500 and the message
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
