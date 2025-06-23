from faker import Faker


class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    COURIER_URL = BASE_URL + 'courier/'
    COURIER_LOGIN = COURIER_URL + 'login/'
    ORDERS_URL = BASE_URL + 'orders/'

class ERROR_MESSAGES:
    DATA_ERROR_MESSAGE = "Недостаточно данных для создания учетной записи"
    LOGIN_ERROR_MESSAGE = "Этот логин уже используется. Попробуйте другой."
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    INSUFFICIENT_LOGIN_INFO = "Недостаточно данных для входа"


fake = Faker()

def create_courier_data():
    payload = {
        "login": f"{fake.user_name()}",
        "password": f"{fake.random_int()}",
        "firstName": f"{fake.first_name()}"
    }
    return payload

courier_data = create_courier_data()

def courier_data_without_field():
    payload = {
        "login": "",
        "password": f"{fake.random_int()}",
        "firstName": f"{fake.first_name()}"
    }
    return payload

order_details = [
    {
        "firstName": f"{fake.first_name()}",
        "lastName": f"{fake.last_name()}",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    },
    {
        "firstName": f"{fake.first_name()}",
        "lastName": f"{fake.last_name()}",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["GREY"]
    },
    {
        "firstName": f"{fake.first_name()}",
        "lastName": f"{fake.last_name()}",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK", "GREY"]
    },
    {
        "firstName": f"{fake.first_name()}",
        "lastName": f"{fake.last_name()}",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
    }
]