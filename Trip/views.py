
from django.http import JsonResponse
from django.http import HttpResponse

from django.core import serializers
import json
from django.shortcuts import render
import time
import uuid
from Trip.models import Trip

def generate_unique_id():
    timestamp = int(time.time() * 1e6)
    random_uuid = uuid.uuid4().hex[:6]
    unique_id = f"{timestamp}-{random_uuid}"
    return unique_id



def index(request):
    return render(request, 'index.html')

def addSingleTrip(request):
    if request.method == 'POST':

        trip_name = request.POST.get('TripName')
        trip_description = request.POST.get('TripDescription')
        trip_price = int(request.POST.get('TripPrice'))
        trip_url = request.POST.get('TripUrl')
        trip_num_bookings = int(request.POST.get('TripNumBookings'))

        trip = Trip(
            trip_name=trip_name,
            trip_description=trip_description,
            trip_price=trip_price,
            trip_url=trip_url,
            trip_num_bookings=trip_num_bookings,
            trip_logic_delete=False,
        )
        trip.save()

        return JsonResponse({"status": "success", "message": "Trip created successfully"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})



def delSingleTrip(request):
    if request.method == 'POST':
        try:
            trip_id = request.POST.get('TripId')

            trip = Trip.objects.get(trip_id=trip_id)

            trip.delete()

            return JsonResponse({"status": "success", "message": "Trip deleted successfully"})
        except Trip.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Trip not found"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})


def delAllTrip(request):
    if request.method == 'POST':
        Trip.objects.all().delete()
        return JsonResponse({"status": "success", "message": "All trips deleted successfully"})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})



def updateSingleTrip(request):
    if request.method == 'POST':
        try:
            trip_id = request.POST.get('TripId')

            trip = Trip.objects.get(trip_id=trip_id)

            trip_name = request.POST.get('TripName', trip.trip_name)
            trip_description = request.POST.get('TripDescription', trip.trip_description)
            trip_price = int(request.POST.get('TripPrice', trip.trip_price))
            trip_url = request.POST.get('TripUrl', trip.trip_url)
            trip_num_bookings = int(request.POST.get('TripNumBookings', trip.trip_num_bookings))
            trip_logic_delete = bool(request.POST.get('TripLogicDelete', trip.trip_logic_delete))

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

def getSingleTrip(request):
    if request.method == 'POST':
        body = request.body
        body = json.loads(request.body)
        tripID = int(request.POST.get("TripID"))

        # getSingleOneTrip
        trip = Trip.objects.get(trip_id=tripID)


        # 将model对象序列化为JSON格式
        json_data = serializers.serialize('json', trip)

        # 将json data转换为json对象
        json_body = json.loads(json_data)
        response = HttpResponse(json_body, content_type='application/json')

def getTop10Trips(request):
    if request.method == 'POST':

        Trips= Trip.objects.all().order_by('-trip_num_bookings')[:10]
        json_data = serializers.serialize('json', )

        # 将json data转换为json对象
        json_body = json.loads(json_data)

        # 创建HTTP响应对象，将JSON格式的数据作为响应内容
        response = HttpResponse(json_body, content_type='application/json')
        return response



def getAllTrips(request):
    if request.method == 'GET':
        trips = Trip.objects.all()

        # 将QuerySet对象序列化为JSON格式
        json_data = serializers.serialize('json', trips)

        # 将JSON数据转换为JSON对象
        json_body = json.loads(json_data)

        # 返回JSON响应
        return JsonResponse({"status": "success", "data": json_body})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})





