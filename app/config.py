import os

class Settings:
    # App info
    APP_NAME = "Accesco Chatbot"
    ENV = os.getenv("ENV", "development")

    # Database (Supabase / Render / Local)
    DATABASE_URL = os.getenv("DATABASE_URL")

    # Security (optional, future use)
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

settings = Settings()
