
from django.http import JsonResponse
from django.http import HttpResponse

from django.core import serializers
import json
from django.shortcuts import render
import time
import uuid
from Trip.models import Trip
from django.views.decorators.csrf import csrf_exempt

def generate_unique_id():
    timestamp = int(time.time() * 1e6)
    random_uuid = uuid.uuid4().hex[:6]
    unique_id = f"{timestamp}-{random_uuid}"
    return unique_id



def index(request):
    return render(request, 'index.html')

@csrf_exempt
def addSingleTrip(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        trip_name = data.get('TripName')
        trip_description = data.get('TripDescription')
        trip_price = data.get('TripPrice')
        trip_url = data.get('TripUrl')

        trip = Trip(
            trip_name=trip_name,
            trip_description=trip_description,
            trip_price=trip_price,
            trip_url=trip_url,
            trip_num_bookings=0,
            trip_logic_delete=False,
        )
        trip.save()

        return JsonResponse({"status": "success", "message": "Trip created successfully"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})


@csrf_exempt
def delSingleTrip(request):
    if request.method == 'POST':
        try:

            data = json.loads(request.body)

            trip_id = data.get('TripId')

            trip = Trip.objects.get(pk=trip_id)

            trip.delete()

            return JsonResponse({"status": "success", "message": "Trip deleted successfully"})
        except Trip.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Trip not found"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def delAllTrip(request):
    if request.method == 'POST':
        Trip.objects.all().delete()
        return JsonResponse({"status": "success", "message": "All trips deleted successfully"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})


@csrf_exempt
def updateSingleTrip(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            trip_id = data.get('TripId')

            trip = Trip.objects.get(pk=trip_id)

            trip_name = data.get('TripName', trip.trip_name)
            trip_description = data.get('TripDescription', trip.trip_description)
            trip_price = data.get('TripPrice', trip.trip_price)
            trip_url = data.get('TripUrl', trip.trip_url)
            trip_num_bookings = data.get('TripNumBookings', trip.trip_num_bookings)
            trip_logic_delete = data.get('TripLogicDelete', trip.trip_logic_delete)

            trip.trip_name = trip_name
            trip.trip_description = trip_description
            trip.trip_price = trip_price
            trip.trip_url = trip_url
            trip.trip_num_bookings = trip_num_bookings
            trip.trip_logic_delete = trip_logic_delete
            trip.save()

            return JsonResponse({"status": "success", "message": "Trip updated successfully"})
        except Trip.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Trip not found"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})


@csrf_exempt
def getSingleTrip(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        trip_id = data.get('TripId')

        try:
            # getSingleOneTrip
            trip = Trip.objects.get(pk=trip_id)

            # 将model对象序列化为JSON格式
            json_data = serializers.serialize('json', [trip])

            # 将json data转换为json对象
            json_body = json.loads(json_data)

            # 返回JSON响应
            return JsonResponse({"status": "success", "data": json_body})
        except Trip.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Trip not found"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})
@csrf_exempt
def getTop10Trips(request):
    if request.method == 'POST':

        # 获取按 trip_num_bookings 降序排列的前10个Trip对象
        trips = Trip.objects.all().order_by('-trip_num_bookings')[:10]

        # 将QuerySet对象序列化为JSON格式
        json_data = serializers.serialize('json', trips)

        # 将json data转换为json对象
        json_body = json.loads(json_data)

        # 返回JSON响应
        return JsonResponse({"status": "success", "data": json_body})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})


@csrf_exempt
def getAllTrips(request):
    if request.method == 'POST':
        trips = Trip.objects.all()

        # 将QuerySet对象序列化为JSON格式
        json_data = serializers.serialize('json', trips)

        # 将JSON数据转换为JSON对象
        json_body = json.loads(json_data)

        # 返回JSON响应
        return JsonResponse({"status": "success", "data": json_body})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})





