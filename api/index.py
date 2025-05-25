from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json

# Load student marks from JSON file
with open("q-vercel-python.json", "r") as f:
    student_data = json.load(f)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        names = query.get("name", [])

        marks = [student_data.get(name, None) for name in names]

        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode())
