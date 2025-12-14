import os

class Settings:
    # App
    APP_NAME = "Accesco Chatbot"
    ENV = os.getenv("ENV", "development")

    # Database
    DATABASE_URL = os.getenv("postgresql://accesco_chatbot_user:VkYQHnBDYuynrfoCVIOCNuf0w83nnkCs@dpg-d4v66deuk2gs7397bj2g-a/accesco_chatbot")

    # Dialogflow
    DIALOGFLOW_PROJECT_ID = os.getenv("acceso-iakw")

    # Security (future)
    SECRET_KEY = os.getenv("U7lkuEXEm8", "dev-secret")

settings = Settings()