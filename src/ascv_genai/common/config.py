from decouple import config

# Example of how to use python-decouple to manage environment variables
# Create a .env file in the root of the project to store your secrets.
#
# .env file example:
# OPENAI_API_KEY="your-secret-key"
# VECTOR_DB_PATH="./chroma_db"

OPENAI_API_KEY = config("OPENAI_API_KEY", default="")
VECTOR_DB_PATH = config("VECTOR_DB_PATH", default="./chroma_db")
REDIS_URL = config("REDIS_URL", default="redis://localhost:6379/0")

# Logging configuration
LOG_LEVEL = config("LOG_LEVEL", default="INFO")
