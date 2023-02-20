from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

import json
from django.http import HttpResponse


def index(request):

    #常规的网络请求 一般使用get/post
    #因为我负责的是商品模块,为了方便展示数据，我会检查当前请求若为GET返回商品信息，方便进行演示进行演示

    #针对GET方法
    #假设一个GET请求是这样子的

    #http://localhost:8000/GroupProjectCode?getAllTrips=1&a=1&b=2&c=3
    #当getAllTrips=1的时候 我就默认前端想要返回所有的商品信息



    #实际应该有post请求 用json对象来解析post内容

    #返回一个json



    if request.method == 'GET':
        body = request.body
        # body = json.loads(request.body)
        getAllTripsStatus = int(request.GET.get("getAllTrips"))

        if getAllTripsStatus == 1:
            print("去查sql lite 返回所有数据")

            print(request.GET.get("c"))
            #去查数据库 query

            #conn

            # res


            #组装成数据结构
            #return







    return HttpResponse("保佑大家IT这门课拿A ！！！  保佑大家IT这门课拿A ！！！  保佑大家IT这门课拿A ！！！ 保佑大家IT这门课拿A ！！！ ")