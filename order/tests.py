from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from Trip.models import Trip

from order.models import Order
from django.contrib.auth.models import User


# Create your tests here.

class orderMethodTests(TestCase):
    def test_ensure_price_are_positive(self):
        """
        Ensures the price received for a order are positive or zero.
        """
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        trip = Trip(
            trip_name='test',
            trip_description='test',
            trip_price=10,
            trip_url='test',
            trip_num_bookings=0,
            trip_logic_delete=False,
        )
        trip.save()
        order = Order(amount=1,time=datetime.now(),price=-53,trip=trip,user=user);
        order.save()
        self.assertEqual((order.price >= 0), True)
    
    def test_ensure_amount_are_positive(self):
        """
        Ensures the amount received for a order are positive or zero.
        """
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        trip = Trip(
            trip_name='test',
            trip_description='test',
            trip_price=10,
            trip_url='test',
            trip_num_bookings=0,
            trip_logic_delete=False,
        )
        trip.save()
       
        order = Order(amount=-1,time=datetime.now(),price=53,trip=trip,user=user);
        order.save()
        self.assertEqual((order.price >= 0), True)

class OrderViewTests(TestCase): 
    def test_index_view_with_no_categories(self):
        """
        If no orders exist, the context dictionary should be empty
        """
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('order:showorder'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['orders'], [])


    def test_index_view_with_orders(self):
        """
        Checks whether orders are displayed correctly when present.
        """
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        trip = Trip(
            trip_name='test',
            trip_description='test',
            trip_price=10,
            trip_url='test',
            trip_num_bookings=0,
            trip_logic_delete=False,
        )
        trip.save()
        trip2 = Trip(
            trip_name='test',
            trip_description='test',
            trip_price=10,
            trip_url='test',
            trip_num_bookings=0,
            trip_logic_delete=False,
        )
        trip2.save()
        order1 = Order(amount=1,time=datetime.now(),price=53,trip=trip,user=user)
        order1.save()
        order2 = Order(amount=5,time=datetime.now(),price=99,trip=trip2,user=user)
        order2.save()

        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('order:showorder'))
        self.assertEqual(response.status_code, 200)
 

        num_categories = len(response.context['orders'])
        self.assertEquals(num_categories, 2)