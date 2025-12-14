from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.routers.webhook import router as webhook_router

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👇 ROOT URL → CHATBOT
@app.get("/", response_class=HTMLResponse)
def show_chat():
    return templates.TemplateResponse(
        "chat.html",
        {"request": {}}
    )

# 👇 DIALOGFLOW WEBHOOK
app.include_router(webhook_router)