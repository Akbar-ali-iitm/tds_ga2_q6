import json
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler

# Load the data once
with open("q-vercel-python.json", "r") as f:
    student_data = json.load(f)

# Create a lookup dictionary: name -> marks
name_to_marks = {entry["name"]: entry["marks"] for entry in student_data}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Extract query params (e.g. ?name=X&name=Y)
        query = parse_qs(self.path.split('?', 1)[1] if '?' in self.path else '')
        names = query.get("name", [])

        # Get marks for each name
        marks = [name_to_marks.get(n, None) for n in names]

        # Return a JSON object (not a raw list!)
        result = { "marks": marks }
        self.wfile.write(json.dumps(result).encode())
