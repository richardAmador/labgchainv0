import os
import instructor
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

from langchain_openai.chat_models import ChatOpenAI

load_dotenv()

portkey_client = instructor.from_openai(
    OpenAI(
        api_key=os.getenv("PORTKEY_API_KEY"),
        base_url=os.getenv("PORTKEY_URL")
    )
)

chat = ChatOpenAI(model_name = 'gpt-4', 
                  model_kwargs = {'seed':365}, 
                  temperature = 0, 
                  max_tokens = 100)
