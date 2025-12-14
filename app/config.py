import os

class Settings:
    # App
    APP_NAME = "Accesco Chatbot"
    ENV = os.getenv("ENV", "development")

    # Database
    DATABASE_URL = os.getenv("DATABASE_URL")

    # Dialogflow
    DIALOGFLOW_PROJECT_ID = os.getenv("DIALOGFLOW_PROJECT_ID")

    # Security (future)
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

settings = Settings()