from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from GroupProjectCode import models
from GroupProjectCode.models import Trip
from GroupProjectCode.models import Order


def index(request):
    return HttpResponse(
        "保佑大家IT这门课拿A ！！！  保佑大家IT这门课拿A ！！！  保佑大家IT这门课拿A ！！！ 保佑大家IT这门课拿A ！！！ ")


def manage_addtrips(request):
    if request.method == "GET":
        return render(request, "manage_addtrips.html")
    # Get user submitted data
    # Trip_id = request.POST.get("Trip_id")
    tripname = request.POST.get("tripname")
    introduction = request.POST.get("introduction")
    image_url = request.FILES.get("image_url")
    # booked_num = request.POST.get("booked_num")
    Trip_price = request.POST.get("Trip_price")
    # Add to database
    Trip.objects.create(
        tripname=tripname,
        introduction=introduction,
        image_url=image_url,
        Trip_price=Trip_price, )

    return HttpResponse("添加成功")


def manage_orders(request):
    # show all orders
    data_list = Order.objects.all()
    return render(request, "manage_orders.html", {"data_list": data_list})


def delete_orders(request):
    # delete orders
    delete_Order_id = request.GET.get('delete_Order_id')
    Order.objects.filter(Order_id=delete_Order_id).delete()
    return redirect("/manage_orders/")


def update_orders(request, update_Order_id):
    if request.method == "GET":
        row_object = models.Order.objects.filter(Order_id=update_Order_id).first()
        # print(row_object.Order_id, row_object.amount, row_object.time, row_object.status, row_object.Order_price)
        return render(request, 'update_orders.html', {"row_object": row_object})
    # update orders
    amount = request.POST.get("amount")
    models.Order.objects.filter(Order_id=update_Order_id).update(amount=amount)

    time = request.POST.get("time")
    models.Order.objects.filter(Order_id=update_Order_id).update(time=time)

    status = request.POST.get("status")
    models.Order.objects.filter(Order_id=update_Order_id).update(status=status)

    price = request.POST.get("price")
    models.Order.objects.filter(Order_id=update_Order_id).update(Order_price=price)
    return redirect("/manage_orders/")
