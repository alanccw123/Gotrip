import datetime
from django.http import HttpResponse
from django.shortcuts import render
from order.models import Order

# Create your views here.
def index(request):
    # return HttpResponse("保佑大家IT这门课拿A ！！！  保佑大家IT这门课拿A ！！！  保佑大家IT这门课拿A ！！！ 保佑大家IT这门课拿A ！！！ ")
    return render(request, 'index.html')

def order(request):
    user_id = 1
    # user_id = request.user.id
    order_list = Order.objects.filter(user=user_id)
    context_dict = {}
    context_dict['orders'] = order_list
    return render(request, 'order.html', context=context_dict)


def makeorder(request):
    trip_id = request.GET['trip_id']
    amount = int(request.GET['amount'])
    user_id = request.user.id
    # price = Trip.objects.filter(id=trip_id)[0].price
    # user_id = 1
    price = 55
    total = price * amount

    new_order = Order(amount=amount, time=datetime.now(),price=total,trip_id=trip_id, user_id=user_id)
    new_order.save()

    # trip = Trip.objects.get(pk=trip_id)
    # trip.bookednum += amount
    # trip.save()

    return HttpResponse('success')

def cancelorder(request):
    order_id = request.GET['order_id']

    order = Order.objects.get(id=order_id)
    order.status = 'cancelled'
    order.save()

    return HttpResponse(order.status)