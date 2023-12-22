import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

from entry_sheet import EntrySheet
from mock_interview import MockInterview

class Message(BaseModel):
    role: str
    content: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/entry-sheet")
async def entry_sheet(question: str, content: str):
    res = await EntrySheet(question, content)
    return {"content": res}


@app.post("/mock-interview")
async def mock_interview(occupation: str, user: Optional[List[str]] = None, question: Optional[List[str]] = None, previous_messages: Optional[List[Message]] = None, isFirst: Optional[bool] = False, isLast: Optional[bool] = False, isEnd: Optional[bool] = False):
    res = await MockInterview(occupation, user, question, previous_messages, isFirst, isLast, isEnd)
    return {"content": res}
