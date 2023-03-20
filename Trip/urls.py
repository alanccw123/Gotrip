from django.urls import path

from . import views

app_name='Trip'

urlpatterns = [
    path('', views.index, name='index'),
    path('addSingleTrip/', views.addSingleTrip, name='addSingleTrip'),
    path('delSingleTrip/', views.delSingleTrip, name='delSingleTrip'),
    path('delAllTrip/', views.delAllTrip, name='delAllTrip'),
    path('updateSingleTrip/', views.updateSingleTrip, name='updateSingleTrip'),
    path('getSingleTrip/', views.getSingleTrip, name='getSingleTrip'),
    path('getTop10Trips/', views.getTop10Trips, name='getTop10Trips'),
    path('getAllTrips/', views.getAllTrips, name='getAllTrips'),
]