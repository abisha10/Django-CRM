from django.urls import path,include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Home, name='home'),
    # path('login-user/', views.Login, name='login'),
    path('logout-user/', views.Logout, name='logout'),
    path('register-user/', views.Register, name='register'),
]