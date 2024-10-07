import os

from chat_manager import ChatManager
from dotenv import load_dotenv
from promptflow.tracing import start_trace
from promptflow.core import AzureOpenAIModelConfiguration

# Load Environment Variables
load_dotenv()

model_config = AzureOpenAIModelConfiguration(
  azure_endpoint=os.getenv("AOAI_ENDPOINT"),
  api_key=os.getenv("AOAI_API_KEY"),
  api_version=os.getenv("AOAI_API_VERSION"),
  azure_deployment=os.getenv("AOAI_DEPLOYMENT")
)


if __name__ == "__main__":
  start_trace()

  chat = ChatManager(config=model_config, temperature=0.7)
  chat_history = []

  while True:
    question = input("\nUSER >> ")
    print("ASSISTANT >> ", end="")

    response = chat(question, chat_history)
    assistant_response = ""

    for chunk in response:
      print(chunk, end="")
      assistant_response += chunk

    chat.update_chat_history("user", question)
    chat.update_chat_history("assistant", assistant_response)

    if assistant_response == "END":
      break