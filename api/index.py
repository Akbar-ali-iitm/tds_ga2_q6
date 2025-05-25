import json
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load and convert the student list to a dict
with open("q-vercel-python.json", "r") as f:
    raw_data = json.load(f)
    students = {entry["name"]: entry["marks"] for entry in raw_data}

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    marks_list = [students.get(n, None) for n in name]
    return JSONResponse(content={"marks": marks_list})
