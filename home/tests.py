from rest_framework.test import APITestCase
from rest_framework import status
from home.models import Restaurant

class RestaurantInfoAPiTest(APITestCase):
    def test_get_restauran_info(self):
        restaurant=Restaurant.objects.create(name='Test Restaurant', address='123 Test St')
        url = '/api/restaurant-info'
        response =self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        data=response.data[0] if isinstance(response.data,list) else response.data
        self.assertEqual(data['name'],'Test Restaurant')
        self.assertEqual(data['address'],'123 Test St')