import unittest
from models.message import Message

class TestMessage(unittest.TestCase):
    def setUp(self):
        self.message = Message('user', 'Hello, world!')

    def test_role(self):
        self.assertEqual(self.message.role, 'user')

    def test_content(self):
        self.assertEqual(self.message.content, 'Hello, world!')

    def test_to_json(self):
        expected = {'role': 'user', 'content': 'Hello, world!'}
        self.assertEqual(self.message.to_json(), expected)


if __name__ == '__main__':
    unittest.main()
