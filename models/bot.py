from dataclasses import dataclass, field
from typing import Callable, List, Dict
from models.ai_model import AIModel
from models.message import Message
from models.function_call import FunctionCall

@dataclass(frozen=True)
class Bot:
    _ai_model: AIModel
    _system_message: Message
    _function_definitions: List[str] = field(default_factory=list)
    _function_resolvers: Dict[str, Callable[..., str]] = field(default_factory=dict)

    def __post_init__(self):
        if self._ai_model is None:
            raise ValueError(f'Bot {self.__class__.__name__} asked for AIModel when `AIModel` is None')
        
        if self._system_message is None:
            raise ValueError(f'Bot {self.__class__.__name__} asked for system_message when `system_message` is None')
        
    def get_system_message_token_count(self) -> int:
        return self.count_tokens([self._system_message])

    def get_completion(self, messages: List[Message]) -> str:
        if messages is None:
            raise ValueError(f'Bot {self.__class__.__name__} asked for completion when `messages` is None')
        
        messages = messages.copy()
        messages.append(self._system_message)

        return self._ai_model.get_ai_completion(self._function_definitions, messages)
    
    def resolve_function(self, function_call: FunctionCall) -> str:
        if function_call is None:
            raise ValueError(f'Bot {self.__class__.__name__} asked for function resolution when `function_call` is None')
        
        if function_call.name is None:
            raise ValueError(f'Bot {self.__class__.__name__} asked for function resolution when `function_call.name` is None')
        
        if function_call.name not in self._function_resolvers:
            raise ValueError(f'Bot {self.__class__.__name__} asked for function resolution when `function_call.name` is not in function_resolvers')
        
        return self._function_resolvers[function_call.name](function_call.arguments)
    
    def count_tokens(self, messages: List[Message]) -> int:
        encoding = self._ai_model.encoding
        string = " ".join([message.content for message in messages])
        length = len(encoding.encode(string))
        return length
    
    def get_token_limit(self) -> int:
        return self._ai_model.context_window_size - self.get_system_message_token_count()
