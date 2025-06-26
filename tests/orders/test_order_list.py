from methods.order_methods import OrderMethods
import allure


class TestListOrders:
    @allure.title('Проверка - в тело ответа возвращается список заказов')
    def test_list_orders(self):
        list_order = OrderMethods.get_orders()
        assert list_order[1] == 200 and isinstance(list_order[0]['orders'], list)
