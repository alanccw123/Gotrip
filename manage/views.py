from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from manage import models
from Trip import models
from order import models
from Trip.models import Trip
from order.models import Order


def manage_trips(request):
    # show all orders
    data_list = Trip.objects.all()
    return render(request, "manage_trips.html", {"data_list": data_list})


def delete_trips(request):
    # delete orders
    delete_trip_id = request.GET.get('delete_trip_id')
    Trip.objects.filter(trip_id=delete_trip_id).delete()
    return redirect("/manage/manage_trips/")


def update_trips(request, update_trip_id):
    if request.method == "GET":
        row_object = models.Trip.objects.filter(trip_id=update_trip_id).first()
        # print(row_object.Order_id, row_object.amount, row_object.time, row_object.status, row_object.Order_price)
        return render(request, 'update_trips.html', {"row_object": row_object})
    # update trips
    trip_name = request.POST.get("trip_name")
    models.Trip.objects.filter(trip_id=update_trip_id).update(trip_name=trip_name)

    trip_description = request.POST.get("trip_description")
    models.Trip.objects.filter(trip_id=update_trip_id).update(trip_description=trip_description)

    trip_price = request.POST.get("trip_price")
    models.Trip.objects.filter(trip_id=update_trip_id).update(trip_price=trip_price)

    trip_logic_delete = request.POST.get("trip_logic_delete")
    models.Trip.objects.filter(trip_id=update_trip_id).update(trip_logic_delete=trip_logic_delete)
    return redirect("/manage/manage_trips/")


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
    trip_logic_delete = request.POST.get("trip_logic_delete")
    # Add to database
    Trip.objects.create(
        trip_name=tripname,
        trip_description=introduction,
        trip_url=image_url,
        trip_price=Trip_price,
        )

    return HttpResponse("添加成功")


def manage_orders(request):
    # show all orders
    data_list = Order.objects.all()
    return render(request, "manage_orders.html", {"data_list": data_list})


def delete_orders(request):
    # delete orders
    delete_Order_id = request.GET.get('delete_Order_id')
    Order.objects.filter(id=delete_Order_id).delete()
    return redirect("/manage/manage_orders/")


def update_orders(request, update_Order_id):
    if request.method == "GET":
        row_object = models.Order.objects.filter(id=update_Order_id).first()
        # print(row_object.Order_id, row_object.amount, row_object.time, row_object.status, row_object.Order_price)
        return render(request, 'update_orders.html', {"row_object": row_object})
    # update orders
    amount = request.POST.get("amount")
    models.Order.objects.filter(id=update_Order_id).update(amount=amount)

    time = request.POST.get("time")
    models.Order.objects.filter(id=update_Order_id).update(time=time)

    status = request.POST.get("status")
    models.Order.objects.filter(id=update_Order_id).update(status=status)

    price = request.POST.get("price")
    models.Order.objects.filter(id=update_Order_id).update(price=price)
    return redirect("/manage/")
