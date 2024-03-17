from typing import Literal
from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''


@pytest.fixture()
def pet_id_fixture():
    test_endpoint = "/store/order"
    test_data = {
    "pet_id": 0,
    }

    response = api_helpers.post_api_data(test_endpoint,test_data)
    print(response.status_code)
    assert response.status_code == 201
    print(response.json())

    response_data = response.json()
    order_id = response_data["id"]
    print(order_id)
    return order_id
    
def test_patch_order_by_id(pet_id_fixture):
    ord_id = pet_id_fixture
    test_endpoint2 = f"/store/order/{ord_id}"
    print(test_endpoint2)
    test_data2 = {
    "status": "available"
    }
    response2 = api_helpers.patch_api_data(test_endpoint2,test_data2)
    print(response2.status_code)
    assert response2.status_code == 200
    print(response2.json())

    response_data_order = response2.json()
    order_id_message = response_data_order["message"]
    print(order_id_message)
    assert order_id_message == "Order and pet status updated successfully"





