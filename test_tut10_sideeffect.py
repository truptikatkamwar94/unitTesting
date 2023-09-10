from tut10 import random_sum,silly
from unittest.mock import call
import mock
#sideeffect
@mock.patch('tut10.random.randint')
def test_random_sum_1(mock_obj):
    mock_obj.side_effect=[3,4]
    assert random_sum()==7

@mock.patch('tut10.random.randint')
def test_random_sum_2(mock_obj):
    mock_obj.side_effect=[3,4]
    assert random_sum()==7
    mock_obj.assert_has_calls(calls=[call(1,10),call(1,7)])#used to check,we are passing correct arguments or not

#multiple mock patch
@mock.patch('tut10.random.randint')
@mock.patch('tut10.time.time')
@mock.patch('tut10.requests.get')
def test_silly(mock_request_get,mock_time,mock_randint):
    test_params={
        "timestamp":123,
        "number":5
    }
    mock_time.return_value=test_params["timestamp"]
    mock_randint.return_value=test_params["number"]
    mock_request_get.return_value=mock.Mock(**{"status_code":200,"json.return_value":{"args":test_params}})
    assert silly()==test_params

