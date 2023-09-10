from tut9_sample_ import guess_number,grt_ip

import mock
import pytest
@pytest.mark.parametrize('_input,expected',[(3,'You won!'),(4,'You lost!')])
@mock.patch('tut9_sample_.rolll_dice')
def test_guess_number(mock_obj,_input,expected):
    mock_obj.return_value=3
    assert guess_number(_input)==expected

@mock.patch('tut9_sample_.requests.get')
def test_get_ip(mock_obj):
    mock_responce=mock.Mock(**{"status_code":200,"json.return_value":{"ip":"0:100:0"}})
    mock_obj.return_value=mock_responce
    assert grt_ip()=="0:100:0"
    mock_obj.assert_called_once_with("https://api.ipify.org?format=json")

