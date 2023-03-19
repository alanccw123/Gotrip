from datetime import datetime
from django.test import TestCase
from django.urls import reverse

from order.models import Order

# Create your tests here.

class orderMethodTests(TestCase):
    def test_ensure_price_are_positive(self):
        """
        Ensures the price received for a order are positive or zero.
        """
        order = Order(amount=1,time=datetime.now(),price=-53,trip=1,user=1);
        order.save()
        self.assertEqual((order.price >= 0), True)
    
    def test_ensure_amount_are_positive(self):
        """
        Ensures the amount received for a order are positive or zero.
        """
        order = Order(amount=-1,time=datetime.now(),price=53,trip=1,user=1);
        order.save()
        self.assertEqual((order.price >= 0), True)

class OrderViewTests(TestCase): 
    def test_index_view_with_no_categories(self):
        """
        If no categories exist, the context dictionary should be empty
        """
        response = self.client.get(reverse('order:showorder'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['orders'], [])


    def test_index_view_with_orders(self):
        """
        Checks whether orders are displayed correctly when present.
        """
        order1 = Order(amount=1,time=datetime.now(),price=53,trip='Spain',user=1)
        order1.save()
        order2 = Order(amount=5,time=datetime.now(),price=99,trip='Italy',user=1)
        order2.save()

        response = self.client.get(reverse('order:showorder'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Spain')
        self.assertContains(response, 'Italy')

        num_categories = len(response.context['orders'])
        self.assertEquals(num_categories, 2)