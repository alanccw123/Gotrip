from datetime import datetime
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from GroupProjectCode.models import Order


def index(request):
    # return HttpResponse("保佑大家IT这门课拿A ！！！  保佑大家IT这门课拿A ！！！  保佑大家IT这门课拿A ！！！ 保佑大家IT这门课拿A ！！！ ")
    return render(request, 'index.html')

def order(request):
    query_userid = 1
    order_list = Order.objects.filter(user=query_userid)
    context_dict = {}
    context_dict['orders'] = order_list
    return render(request, 'order.html', context=context_dict)

def makeorder(request):
    trip_id = request.GET['trip_id']
    amount = int(request.GET['amount'])
    # user_id = request.user.id
    # price = Trip.objects.filter(id=trip_id)[0].price
    user_id = 1
    price = 55
    total = price * amount

    new_order = Order(amount=amount, time=datetime.now(),price=total,trip=trip_id, user=user_id)
    new_order.save()

    return HttpResponse('success')