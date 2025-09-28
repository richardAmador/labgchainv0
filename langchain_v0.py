import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

chat = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("PORTKEY_API_KEY"),
    base_url=os.getenv("PORTKEY_URL"),
    temperature=0,
    max_tokens=100,
    seed=365,
)

print(chat.invoke("Say hello in one short sentence."))