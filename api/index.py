import json
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler

# Load student data once
with open("q-vercel-python.json", "r") as f:
    student_data = json.load(f)

name_to_marks = {entry["name"]: entry["marks"] for entry in student_data}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        query = parse_qs(self.path[6:])  # Strip "/api?" from path
        names = query.get("name", [])
        marks = [name_to_marks.get(n, None) for n in names]

        response = { "marks": marks }
        self.wfile.write(json.dumps(response).encode())
