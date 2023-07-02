import unittest
from unittest.mock import patch
from get_completion import get_completion

class TestGetCompletion(unittest.TestCase):
    @patch('openai.ChatCompletion.create')
    def test_get_completion(self, mock_create):

        mock_choice = mock_create.return_value.choices[0]
        mock_choice.message.content = "Mock response"
        
        prompt = "Test prompt"
        result = get_completion(prompt)
        
        mock_create.assert_called_once_with(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are a helpful assistant who speaks in cockney slang."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        self.assertEqual(result, "Mock response")

# if __name__ == '__main__':
#     unittest.main()
