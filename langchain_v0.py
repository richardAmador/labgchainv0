import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import instructor
from openai import OpenAI
from portkey_ai import Portkey
from pydantic import BaseModel

# Load env vars
load_dotenv()

# --- Example 1: Instructor + Portkey ---
portkey_client = instructor.from_openai(
    OpenAI(
        api_key=os.getenv("PORTKEY_API_KEY"),
        base_url=os.getenv("PORTKEY_URL")
    )
)

# --- Example 2: LangChain + Azure OpenAI ---
chat = ChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0,
    max_tokens=100,
    seed=365,
)

resp = chat.invoke("Say hello in one short sentence.")
print(resp)