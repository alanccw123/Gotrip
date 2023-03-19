from django.urls import path,re_path
from sign_up import views
urlpatterns = [
    path('', views.index, name='index'),
    #path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/',
    views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]