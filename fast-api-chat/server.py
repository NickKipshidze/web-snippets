from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Simple array for now
comments: list = [
    {"user": "server", "content": "server started"}
]

origins: list = [
    # Origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def read_root() -> dict:
    return {
        "info": "This is a chat API built by Nick Kipshidze"
    }

@app.get("/comments")
def read_comments() -> list:
    return comments

@app.post("/comment")
def create_comment(comment: dict) -> bool:
    comments.append(comment)
    return True