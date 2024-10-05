from typing import Any
from promptflow.tracing import trace
from promptflow.core import Prompty, AzureOpenAIModelConfiguration

class ChatManager:
  def __init__(self, config: AzureOpenAIModelConfiguration, temperature: float = 0.5):
    self.config = config
    self.temperature = temperature

  @trace
  def __call__(self, *args: Any, **kwds: Any) -> str:
    """Chat Entry Point"""

    # Extract Arguments
    if not isinstance(args[0], str):
      raise ValueError("The first argument must be a string")
    
    if not isinstance(args[1], list):
      raise ValueError("The second argument must be a list")
    
    question = args[0]
    chat_history = args[1] or []

    override_prompt_config = {
      "configuration": self.config,
      "paramenters": {
        "temperature": self.temperature
      }
    }

    prompty = Prompty.load(
      source="./prompts/sample_chat.prompty",
      override_model=override_prompt_config
    )

    output = prompty(
      question=question, 
      chat_history=chat_history
    )

    return output