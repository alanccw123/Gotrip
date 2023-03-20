from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('showorder', views.order, name='showorder'),
    path('makeorder', views.makeorder, name='makeorder'),
    path('cancelorder', views.cancelorder, name='cancelorder')
]