import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("AZURE_ENDPOINT")
    KEY = os.getenv("AZURE_DOCINT_KEY")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_KEY")
    CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME")