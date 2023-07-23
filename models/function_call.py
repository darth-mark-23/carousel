from dataclasses import dataclass

@dataclass
class FunctionCall:
    name: str
    arguments: dict

    def __post_init__(self):
        if self.name == "" or self.name == None:
            raise AttributeError("FunctionCall.name cannot be empty.")
            
        if self.arguments == {} or self.arguments == None:
            raise AttributeError("FunctionCall.arguments cannot be empty.")
        
