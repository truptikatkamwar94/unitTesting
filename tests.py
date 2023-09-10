import unittest
from unittest.mock import patch,MagicMock
from main import len_joke,get_joke


class TestJoke(unittest.TestCase):
    @patch('main.get_joke')
    def test_len_joke(self,mock_get_joke):
        mock_get_joke.return_value = "test"
        self.assertEquals(len_joke(),4)

    @patch('main.requests')
    def test_get_joke(self,mock_requests):
        mock_responce=MagicMock()
        mock_responce.status_code=200
        mock_responce.json.return_value={'value':{'joke':'hello world'}}
        mock_requests.get.return_value=mock_responce
        self.assertEqual(get_joke(),'hello world')


    @patch('main.requests')
    def test_not_get_joke(self,mock_requests):
        mock_responce=MagicMock()
        mock_responce.status_code=403
        mock_responce.json.return_value={'value':{'joke':'world'}}
        mock_requests.get.return_value=mock_responce
        self.assertEqual(get_joke(),'No joke')

