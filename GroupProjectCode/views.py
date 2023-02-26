from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.http import HttpResponse

from GroupProjectCode.models import Trip


def index(request):
    return HttpResponse(
        "保佑大家IT这门课拿A ！！！  保佑大家IT这门课拿A ！！！  保佑大家IT这门课拿A ！！！ 保佑大家IT这门课拿A ！！！ ")


def manage_addtrips(request):
    if request.method == "GET":
        return render(request, "manage_addtrips.html")

    # 获取用户提交的数据
    id = request.POST.get("id")
    tripname = request.POST.get("tripname")
    introduction = request.POST.get("introduction")
    imageurl = request.POST.get("imageurl")
    bookednum = request.POST.get("bookednum")
    price = request.POST.get("price")
    # 添加到数据库
    Trip.objects.create(id=id,
                        tripname=tripname,
                        introduction=introduction,
                        imageurl=imageurl,
                        bookednum=bookednum,
                        price=price,)

    return HttpResponse("添加成功")


def manage_reviews(request):
    return render(request, "manage_reviews.html")
