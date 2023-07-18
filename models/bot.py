from dataclasses import dataclass, field
from models.ai_model import AIModel
from models.message import Message

@dataclass(frozen=True)
class Bot:
    _ai_model: AIModel
    _system_message: Message
    _function_definitions: list[str] = field(default_factory=list[str])

    def __post_init__(self):
        if ( self._ai_model is None ):
            raise Exception('Bot ' + self.__class__.__name__ + ' asked for AIModel when `AIModel` is None')
        
        if ( self._system_message is None ):
            raise Exception('Bot ' + self.__class__.__name__ + ' asked for system_message when `system_message` is None')
        
    def get_system_message_token_count(self) -> int:
        return self.count_tokens([self._system_message])

    def get_completion(self, messages) -> str:
        if (messages is None):
            raise Exception('Bot ' + self.__class__.__name__ + ' asked for completion when `messages` is None')
        
        messages.append(self._system_message)

        return self._ai_model.get_ai_completion(self._function_definitions, messages)
    
    def count_tokens(self, messages: list[Message]) -> int:
        encoding = self._ai_model.encoding
        string = " ".join([message.content for message in messages])
        length = len(encoding.encode(string))
        return length
    
    def get_token_limit(self) -> int:
        return self._ai_model.context_window_size - self.get_system_message_token_count()