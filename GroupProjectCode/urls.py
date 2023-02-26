from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('manage_addtrips/', views.manage_addtrips),
    path('manage_reviews/', views.manage_reviews),

]
