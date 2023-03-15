from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


from django.http import HttpResponse


def index(request):
    return HttpResponse("保佑大家IT这门课拿A ！！！  保佑大家IT这门课拿A ！！！  保佑大家IT这门课拿A ！！！ 保佑大家IT这门课拿A ！！！ ")