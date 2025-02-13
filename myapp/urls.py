from django.urls import path,include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Home, name='home'),
    # path('login-user/', views.Login, name='login'),
    path('logout-user/', views.Logout, name='logout'),
    path('register-user/', views.Register, name='register'),
    path('record/<int:pk>', views.Customer_Record, name='record'),
    path('delete/<int:pk>', views.Delete_Record, name='delete'),
    path('add/', views.Add_Record, name='add_record'),
    path('update/<int:pk>', views.Update, name='update'),
]