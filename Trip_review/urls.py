from django.urls import path
from . import views

urlpatterns = [
    path(r'^review/', views.review),
    path(r'^review_delete/', views.review_delete)
]
