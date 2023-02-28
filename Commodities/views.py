from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from Commodities.models import Commodities
from django.core import serializers
import json

def index(request):

    if request.method == 'GET':
        body = request.body
        # body = json.loads(request.body)
        getAllTripsStatus = int(request.GET.get("getAllTrips"))
        getTop10Trips = int(request.GET.get("getTop10Trips"))

        if getAllTripsStatus == 1 and getTop10Trips == 0:
            # 获取所有的model对象
            commodities = Commodities.objects.all()

            # 将model对象序列化为JSON格式
            json_data = serializers.serialize('json', commodities)

            # 将json data转换为json对象
            json_body = json.loads(json_data)

            # 创建HTTP响应对象，将JSON格式的数据作为响应内容

            response = HttpResponse(json_body, content_type='application/json')
        if getTop10Trips == 1 and getAllTripsStatus == 0:
            # 获取所有的model对象,并根据被预订的次数返回top10
            commodities = Commodities.objects.all().order_by('-commodities_num_bookings')[:10]

            # 将model对象序列化为JSON格式
            json_data = serializers.serialize('json', commodities)

            # 将json data转换为json对象
            json_body = json.loads(json_data)

            # 创建HTTP响应对象，将JSON格式的数据作为响应内容

            response = HttpResponse(json_body, content_type='application/json')



        return response

#Django是如何做路由
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)