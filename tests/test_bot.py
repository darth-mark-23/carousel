import unittest
from unittest.mock import Mock, MagicMock
from models.bot import Bot 

class TestBot(unittest.TestCase):
    def setUp(self):
        self.mock_ai_model = MagicMock()
        self.mock_system_message = Mock()
        self.mock_message_1 = Mock()
        self.mock_message_2 = Mock()
        self.bot = Bot(self.mock_ai_model, self.mock_system_message)

    def test_get_system_message_token_count(self):
        self.mock_ai_model.encoding.encode.return_value = [1, 2, 3]
        self.mock_system_message.content = "Mock message"
        result = self.bot.get_system_message_token_count()
        self.assertEqual(result, 3)

    def test_get_completion(self):
        self.mock_ai_model.get_ai_completion.return_value = "Mocked completion"
        result = self.bot.get_completion([self.mock_message_1, self.mock_message_2])
        self.assertEqual(result, "Mocked completion")

    def test_count_tokens(self):
        self.mock_ai_model.encoding.encode.return_value = [1, 2, 3, 4, 5]
        self.mock_message_1.content = "Mock message 1"
        self.mock_message_2.content = "Mock message 2"
        result = self.bot.count_tokens([self.mock_message_1, self.mock_message_2])
        self.assertEqual(result, 5)

    def test_get_token_limit(self):
        self.mock_ai_model.context_window_size = 100
        self.mock_ai_model.encoding.encode.return_value = [1, 2, 3]
        self.mock_system_message.content = "Mock message"
        result = self.bot.get_token_limit()
        self.assertEqual(result, 97)

    def test_ai_model_none(self):
        with self.assertRaises(Exception):
            Bot(None, self.mock_system_message)

    def test_system_message_none(self):
        with self.assertRaises(Exception):
            Bot(self.mock_ai_model, None)

    def test_get_completion_messages_none(self):
        with self.assertRaises(Exception):
            self.bot.get_completion(None)


if __name__ == '__main__':
    unittest.main()
