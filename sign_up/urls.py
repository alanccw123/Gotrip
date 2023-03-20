from django.urls import path,re_path
from sign_up import views

app_name="sign_up"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]