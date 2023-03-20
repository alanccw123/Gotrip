import datetime
from django.http import HttpResponse
from django.shortcuts import render
from Trip.models import Trip
from order.models import Order
from django.contrib.auth.decorators import login_required


# Create your views here.

# displaying all order for a given user
# @login_required

def order(request):
    user_id = request.user.id
    order_list = Order.objects.filter(user_id=user_id)
    context_dict = {}
    context_dict['orders'] = order_list
    return render(request, 'order.html', context=context_dict)


# making a new order
def makeorder(request):
    # get trip_id and no of trips from the request
    trip_id = request.GET['trip_id']
    amount = int(request.GET['amount'])
    user_id = request.user.id
    price = Trip.objects.filter(pk=trip_id)[0].trip_price
    total = price * amount

    #create the new order
    new_order = Order(amount=amount, time=datetime.now(),price=total,trip_id=trip_id, user_id=user_id)
    new_order.save()

    # increment the no of bookings in the Trip model
    trip = Trip.objects.get(pk=trip_id)
    trip.trip_num_bookings += amount
    trip.save()

    return HttpResponse('success')

# cancelling an order
def cancelorder(request):
    order_id = request.GET['order_id']

    #change status field to 'cancelled'
    order = Order.objects.get(id=order_id)
    order.status = 'cancelled'
    order.save()

    return HttpResponse(order.status)