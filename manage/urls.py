from django.urls import path

from . import views

app_name='manage'

urlpatterns = [
    path('', views.manage_addtrips, name='index'),
    path('manage_addtrips/', views.manage_addtrips),
    path('manage_orders/', views.manage_orders),
    path('manage_orders/delete/', views.delete_orders),
    path('manage_orders/<int:update_Order_id>/update/', views.update_orders),
]
