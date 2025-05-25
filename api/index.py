from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Load student marks from the JSON file (1 level above this script)
        path = os.path.join(os.path.dirname(__file__), '../q-vercel-python.json')
        with open(path, 'r') as f:
            student_data = json.load(f)

        # Parse URL query: ?name=X&name=Y
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        names = query.get("name", [])

        # Return marks in order
        marks = [student_data.get(name, None) for name in names]

        # Enable CORS
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Send response
        self.wfile.write(json.dumps({"marks": marks}).encode())
