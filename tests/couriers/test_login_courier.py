import allure
from data import *
from conftests import *


class TestLoginCourier:
    @allure.title('Проверка курьер может авторизоваться и успешный запрос возвращает id')
    def test_login_courier(self, courier_create):
        payload = data.courier_data
        courier_response = CourierMethods.login_courier(payload)
        assert courier_response[1] == 200  and courier_response[0]['id']

    @allure.title('Проверка система вернёт ошибку, если неправильно указать логин или пароль и если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_login_courier_with_non_existent_data(self):
        payload = data.create_courier_data()
        courier_response = CourierMethods.login_courier(payload)
        assert (courier_response[1] == 404  and
                courier_response[0]['message'] == ERROR_MESSAGES.ACCOUNT_NOT_FOUND)

    @allure.title('Проверка для авторизации нужно передать все обязательные поля и если какого-то поля нет, запрос возвращает ошибку')
    def test_login_courtier_without_any_field(self):
        payload = data.courier_data_without_field()
        courier_response = CourierMethods.login_courier(payload)
        assert (courier_response[1] == 400 and
                courier_response[0]['message'] == ERROR_MESSAGES.INSUFFICIENT_LOGIN_INFO)
