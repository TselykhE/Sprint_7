import requests
import allure
from data import Urls

class CourierMethods:

    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(payload):
        response = requests.post(Urls.COURIER_URL, data=payload)
        return response.json(), response.status_code

    @staticmethod
    @allure.step('Авторизация курьера')
    def login_courier(payload):
        response = requests.post(Urls.COURIER_LOGIN, data=payload)
        return response.json(), response.status_code

    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(id):
        requests.delete(f"{Urls.COURIER_URL}/{id}")
