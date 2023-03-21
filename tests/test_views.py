from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from django.contrib.auth.models import User

class MenuItemViewTest(TestCase):
    def setUp(self) -> None:
        Menu.objects.create(title='Ice Cream', price = 80, inventory = 100)
        Menu.objects.create(title='Samosa', price = 20, inventory = 10)

        User.objects.create_user(username='testuser', password='Mage@2023')

    def test_all(self):
        all_menu_items = Menu.objects.all()
        serialized_items = MenuSerializer(all_menu_items, many=True)

        url = reverse('menu-items')
        token_url = reverse('auth-token')
        token_response = self.client.post(token_url, {'username': 'testuser', 'password': 'Mage@2023'})
        token = token_response.json()['token']
        response = self.client.get(url, HTTP_AUTHORIZATION = f"Token {token}")
        menu_items = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(menu_items), 2)
        self.assertEqual(menu_items, serialized_items.data)