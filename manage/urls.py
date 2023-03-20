from django.urls import path

from . import views
app_name = 'manage'

urlpatterns = [
    # index
    path('', views.manage_orders, name='index'),
    # manage orders
    path('manage_orders/', views.manage_orders),
    path('manage_orders/delete/', views.delete_orders),
    path('manage_orders/<int:update_Order_id>/update/', views.update_orders),
    # manage trips
    path('manage_addtrips/', views.manage_addtrips),
    path('manage_trips/', views.manage_trips),
    path('manage_trips/delete/', views.delete_trips),
    path('manage_trips/<int:update_trip_id>/update/', views.update_trips),

]
