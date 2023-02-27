from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


from django.http import HttpResponse


def comment(request):
    return render(request, 'website.html')