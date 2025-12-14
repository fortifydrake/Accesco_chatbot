import os

DATABASE_URL = os.getenv("postgresql://accesco_chatbot_user:VkYQHnBDYuynrfoCVIOCNuf0w83nnkCs@dpg-d4v66deuk2gs7397bj2g-a/accesco_chatbot")

from sqlalchemy import create_engine

engine = create_engine("postgresql://accesco_chatbot_user:VkYQHnBDYuynrfoCVIOCNuf0w83nnkCs@dpg-d4v66deuk2gs7397bj2g-a/accesco_chatbot")