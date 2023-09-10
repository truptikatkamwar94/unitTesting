from project import ShoppingCart
import pytest
from project_Item_database import ItamDatabase
import mock
@pytest.fixture
def create_obj_fix():
    return ShoppingCart(5)
def test_can_add_item_to_cart(create_obj_fix):
    create_obj_fix.add("Apple")
    assert create_obj_fix.size()==1

def test_when_item_added_then_cart_contains_item(create_obj_fix):
    create_obj_fix.add("Apple")
    assert "Apple" in create_obj_fix.get_items()

def test_when_more_than_max_item_should_fail(create_obj_fix):
    for _ in range(5):
            create_obj_fix.add("Apple")

    with pytest.raises(OverflowError):
         create_obj_fix.add("Apple")
        
def test_can_get_total_price(create_obj_fix):
    print("Testing can get price")
    create_obj_fix.add("apple")
    create_obj_fix.add("orange")
    price_map={"apple":1.0,"orange":2.0}
    assert create_obj_fix.get_total_price(price_map)==3.0


def test_can_get_total_price_mock(create_obj_fix):
    print("Testing can get price")
    create_obj_fix.add("apple")
    create_obj_fix.add("orange")
    itemDtabase=ItamDatabase()
    itemDtabase.get=mock.Mock(return_value=1.0)
    assert create_obj_fix.get_total_price(itemDtabase)==2.0


def test_can_get_total_price_mock_sideEffect(create_obj_fix):
    print("Testing can get price")
    create_obj_fix.add("apple")
    create_obj_fix.add("orange")
    itemDtabase=ItamDatabase()
    def mock_get_item(item:str):
         if item=="apple":
              return 1.0
         if item=="orange":
              return 2.0
    itemDtabase.get=mock.Mock(side_effect=mock_get_item)
    assert create_obj_fix.get_total_price(itemDtabase)==3.0



    # if you want to test particuler test:pytest test_project.py::test_can_get_total_price -s -v
