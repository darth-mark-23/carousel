from dataclasses import dataclass

@dataclass(frozen=True)
class Message:
    role: str
    content: str

    def to_json(self):
        return {'role': self.role, 'content': self.content}
    