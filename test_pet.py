from typing import Literal
from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''
def test_pet_schema():
    test_endpoint = "/pets/1"

    response = api_helpers.get_api_data(test_endpoint)
    print(response.status_code)
    assert response.status_code == 200

    print(response.json())

    # Validate the response schema against the defined schema in schemas.py
    validate(instance=response.json(), schema=schemas.pet)

'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_by_status_200(status: Literal['available', 'pending', 'sold']):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }

    response = api_helpers.get_api_data(test_endpoint, params)

    # Validate the appropriate response code
    assert response.status_code == 200
    print(response.json())

    # Validate the 'status' property in the response is equal to the expected status
    response_json = response.json()
    for pet in response_json:
        assert pet['status'] == status
        print(pet['status'])
    # Validate the schema for each object in the response
    for pet in response_json:
        validate(instance=pet, schema=schemas.pet)

'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases
'''
@pytest.mark.parametrize("pet_id", [-1])
def test_get_by_id_400(pet_id):
    test_endpoint = f"/pets/{pet_id}"
    response = api_helpers.get_api_data(test_endpoint)

    # Validate the appropriate 404 response
    assert response.status_code == 404

    