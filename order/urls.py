from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('showorder', views.order, name='showorder'),
    path('makeorder', views.makeorder, name='makeorder')
]