from dataclasses import dataclass
from services.get_completion import get_completion
from tiktoken import encoding_for_model, Encoding

@dataclass(frozen=True)
class AIModel:
    model_name: str
    context_window_size: int
    completion_function: callable = get_completion

    def __post_init__ (self) -> None:
        if ( self.model_name is None ):
            raise Exception('AIModel ' + self.__class__.__name__ + ' asked for model_name when `model_name` is None')
        
        if ( self.context_window_size is None ):
            raise Exception('AIModel ' + self.__class__.__name__ + ' asked for chat_history_token_limit when `chat_history_token_limit` is None')

    @property
    def encoding(self) -> Encoding:
        return encoding_for_model(self.model_name)
    
    def get_ai_completion(self, function_definitions, messages) -> str:
        if (messages is None):
            raise Exception('Bot ' + self.__class__.__name__ + ' asked for completion when `messages` is None')
        
        return self.completion_function(self.model_name, function_definitions, messages)
