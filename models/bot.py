from services.get_completion import get_completion

class Bot:
    def __init__(self, model, system_message, function_definitions):
        self.model = model
        self.system_message = system_message
        self.function_definitions = function_definitions

    def get_model(self):
        return self.model
    
    def get_system_message(self):
        return self.system_message
    
    def get_function_definitions(self):
        return self.function_definitions

    def get_completion(self, messages):
        if (messages is None):
            raise Exception('Bot ' + self.__class__.__name__ + ' asked for completion when `messages` is None')
        
        return get_completion(self.model, self.function_definitions, messages)