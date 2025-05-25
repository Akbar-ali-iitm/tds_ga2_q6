from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.responses import JSONResponse

app = FastAPI()

# CORS enabled
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Sample exact dataset for demo
students = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 76,
    "David": 88,
    "Eva": 95,
    # ... add up to 100 exactly
}

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    marks_list = [students.get(n, None) for n in name]  # returns `None` if name not found
    return JSONResponse(content={"marks": marks_list})
