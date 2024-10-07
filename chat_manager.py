from typing import Any
from promptflow.tracing import trace
from promptflow.core import Prompty, AzureOpenAIModelConfiguration

class ChatManager:
  def __init__(self, config: AzureOpenAIModelConfiguration, temperature: float = 0.5):
    self.chat_history = []

    override_prompt_config = {
      "configuration": config,
      "paramenters": {
        "temperature": temperature
      }
    }

    self.prompty = Prompty.load(
      source="./prompts/sample_chat.prompty",
      override_model=override_prompt_config
    )

  @trace
  def __call__(self, *args: Any, **kwds: Any) -> str:
    """Chat Entry Point"""

    # Extract Arguments
    if not isinstance(args[0], str):
      raise ValueError("The first argument must be a string")
    
    question = args[0]

    output = self.prompty(
      question=question, 
      chat_history=self.chat_history
    )

    return output
  
  def update_chat_history(self, role: str, content: str):
    self.chat_history.append({ "role": role, "content": content })