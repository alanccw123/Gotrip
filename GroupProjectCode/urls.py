from django.urls import path
from . import views

urlpatterns = [
    path("comment/", views.comment),
    path("delete/", views.delete)

]