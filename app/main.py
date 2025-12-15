from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.routers.webhook import router as webhook_router
from fastapi import Request                                                                                             

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

from app.database import SessionLocal

@app.get("/db-test")
def db_test():
    db = SessionLocal()
    try:
        db.execute("SELECT 1")
        return {"db": "connected"}
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👇 ROOT URL → CHATBOT
@app.get("/", response_class=HTMLResponse)
def show_chat(request: Request):
    return templates.TemplateResponse(
        "chat.html",
        {"request": request}
    )

# 👇 DIALOGFLOW WEBHOOK
app.include_router(webhook_router)