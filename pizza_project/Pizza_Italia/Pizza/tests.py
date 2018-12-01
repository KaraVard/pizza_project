from django.test import TestCase
from.models import Order, Pizza

class Ordertest(TestCase):
    def test_pizza_name(self):
        p_obj = Pizza(name='test_name', pizza_size=20)
        or_obj = Order(pizza= p_obj, pizza_size=30, customer_name='asas', customer_address = 'rrrr')
        self.assertEqual(p_obj.name, or_obj.pizza.name)