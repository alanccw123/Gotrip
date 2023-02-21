from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manage_overview/', views.manage_overview),
    path('manage_detail/', views.manage_detail),

]