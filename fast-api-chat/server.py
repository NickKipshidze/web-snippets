from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import db, json

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def convert_to_dict(array: list[list], keys: list) -> list[dict]:
    dicts: list[dict] = []
    
    for item in array:
        dicts.append({})
        for index, key in enumerate(keys):
            dicts[-1][key] = item[index]
    
    return dicts

@app.get("/")
def read_root() -> dict:
    return {"message": "API is operational", "credits": "Made By Nick Kipshidze"}

@app.get("/comments")
def read_comments() -> list:
    database: list[dict] = convert_to_dict(
        db.read_all(),
        ["id", "content", "author"]
    )
    
    return json.loads(
        json.dumps(
            database
        )
    )

@app.post("/comments/new")
def create_comment(comment: dict) -> dict:    
    if "<" in comment["content"] or ">" in comment["content"] or "<" in comment["author"] or ">" in comment["author"]:
        raise HTTPException(status_code = 403, detail = "No")
    if not comment["content"]:
        raise HTTPException(status_code = 403, detail = "Content is required")
    if not comment["author"]:
        raise HTTPException(status_code = 403, detail = "Author is required")
    
    db.create_comment(
        comment["content"],
        comment["author"]
    )
    
    return {"message": "Comment created"}
