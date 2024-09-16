from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Olá mundo!"}

@app.get("/ping")
async def ping():
    return f'pong - {datetime.now().strftime("%d/%m/%Y - %H:%M")}'
