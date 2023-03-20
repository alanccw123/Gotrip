from django.urls import path
from . import views

app_name = 'Trip_review'

urlpatterns = [
    path(r'^review/', views.review),
    path(r'^review_delete/', views.review_delete)
]
