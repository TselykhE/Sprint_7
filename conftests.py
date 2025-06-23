import pytest
import data
from methods.courier_methods import CourierMethods


@pytest.fixture()
def courier_create():
    payload = data.courier_data
    courier_response = CourierMethods.create_courier(payload)
    yield courier_response
    courier_response_1 = CourierMethods.login_courier(payload)
    id = courier_response_1[0]['id']
    CourierMethods.delete_courier(id)
