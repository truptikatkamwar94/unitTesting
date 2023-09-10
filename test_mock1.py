from unittest import mock
import pytest
from tut9.myapp.sample import guess_number,get_ip


@pytest.mark.parametrize("_input,expected",[(3,"You won!"),(4,"You lost!")])
@mock.patch('tut9.myapp.sample.roll_dics')
def  test_guess_number(mock_roll_dics,_input,expected):
    mock_roll_dics.return_value=3
    assert guess_number(_input)==expected
    mock_roll_dics.assert_called_once()

@mock.patch('tut9.myapp.sample.requests.get')
def test_get_ip(mock_requests_get):
    mock_responce=mock.Mock(**{"status_code":200,"json.return_value":{"origin":"0.0.0.0"}})
    mock_requests_get.return_value=mock_responce
    assert get_ip()=='0.0.0.0'


#or
@mock.patch('tut9.myapp.sample.requests.get')
def test_get_ip1(mock_requests_get):
    mock_requests_get.return_value= mock.Mock(**{"status_code":200,"json.return_value":{"origin":"0.0.0.0"}})
    assert get_ip()=='0.0.0.0'
    mock_requests_get.assert_called_once_with("https.get://httpbin.org/ip")