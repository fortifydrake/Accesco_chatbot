import os

class Settings:
    # App info
    APP_NAME = "Accesco Chatbot"
    ENV = os.getenv("ENV", "development")

    # Database (Supabase / Render / Local)
    DATABASE_URL = os.getenv("postgresql://postgres:@Adit779ya@db.slhrjrvlaukebpmgxipk.supabase.co:5432/postgres")

    # Security (optional, future use)
    SECRET_KEY = os.getenv("U7lkuEXEm8", "dev-secret")

settings = Settings()
