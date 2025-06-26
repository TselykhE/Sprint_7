import requests
import allure
from data import Urls

class OrderMethods:

    @staticmethod
    @allure.step("Создать заказ")
    def post_order(payload):
        response = requests.post(Urls.ORDERS_URL, data=payload)
        return response.json(), response.status_code

    @staticmethod
    @allure.step("Получить заказы")
    def get_orders():
        response = requests.get(Urls.ORDERS_URL)
        return response.json(), response.status_code
