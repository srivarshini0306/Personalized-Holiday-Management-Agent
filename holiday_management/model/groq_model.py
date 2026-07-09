from autogen_ext.models.openai import OpenAIChatCompletionClient
from holiday_management.config.settings import GROQ_API_KEY, MODEL_NAME
from dotenv import load_dotenv

load_dotenv()

model_client = OpenAIChatCompletionClient(
    model=MODEL_NAME,                     # e.g. "llama-3.3-70b-versatile"
    api_key=GROQ_API_KEY,
)