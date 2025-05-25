from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS for all origins on GET requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Generate 100 imaginary students with marks (e.g. Student1, Student2,...)
students = {f"Student{i}": i % 100 + 1 for i in range(1, 101)}

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    # Collect marks for each requested name
    marks_list = [students.get(n, None) for n in name]
    # If a student name is not found, you could either return null or 0 or error - I'll use None
    return JSONResponse(content={"marks": marks_list})
