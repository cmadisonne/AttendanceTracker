from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('clockIn/', views.clockIn, name='clockIn'),
    path('clockOut/', views.clockOut, name='clockOut'),
    path('signUp/', views.signup, name='signUp'),
]