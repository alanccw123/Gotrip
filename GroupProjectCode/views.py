import os

from django.shortcuts import render, redirect
from isort.profiles import django

from GroupProjectCode import models
# Create your views here.

from django.http import HttpResponse

from django.http import HttpResponse


def comment(request):
    review = models.Review.objects.all()
    return render(request, 'website.html', {'review': review})


def comment_add(request):
    if request.method == "POST":
     return render(request, 'website.html')

    content = request.POST.get('content')
    print(content)
    rate = request.POST.get('inlineRadioOptions')
    time = request.POST.get('time')
    models.Review.objects.create(content=content, date=time, score=rate, deleteStatus=2)
    return redirect(request, '/comment/')

def delete(request):
    review = models.Review.objects.all()
    return render(request, 'delete.html', {'review': review})


def delete_d(request):
    d = request.GET.get('tid')
    models.Review.objects.filter(id=d).delete()
    return redirect("/delete/")
