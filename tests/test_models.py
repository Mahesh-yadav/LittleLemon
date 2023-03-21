from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_create_menu_item(self):
        item = Menu.objects.create(title='Ice Cream', price = 80, inventory = 100)
        self.assertEqual(item.title, "Ice Cream")