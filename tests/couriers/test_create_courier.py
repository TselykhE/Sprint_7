import allure

from data import *
from conftests import *


class TestCreateCourier:
    @allure.title('Проверка создания курьера')
    def test_create_courier(self):
        payload = data.courier_data
        courier_response = CourierMethods.create_courier(payload)
        assert courier_response[1] == 201 and courier_response[0]['ok']
        courier_response_1 = CourierMethods.login_courier(payload)
        id = courier_response_1[0]['id']
        CourierMethods.delete_courier(id)


    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    def test_no_create_same_courier(self, courier_create):
        payload = data.courier_data
        courier_response = CourierMethods.create_courier(payload)
        assert (courier_response[1] == 409 and
                courier_response[0]['message'] == ERROR_MESSAGES.LOGIN_ERROR_MESSAGE)

    @allure.title('Проверка невозможности создания курьера без обязательного поля')
    def test_no_create_courier_without_field(self):
        payload = data.courier_data_without_field()
        courier_response = CourierMethods.create_courier(payload)
        assert (courier_response[1] == 400 and
                courier_response[0]['message'] == ERROR_MESSAGES.DATA_ERROR_MESSAGE)