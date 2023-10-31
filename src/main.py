from fastapi import FastAPI

from entry_sheet import EntrySheet

app = FastAPI()

@app.post("/ai")
async def ai(message: str):
  res = await EntrySheet(message)
  return {"message": res}