from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('clockIn/', views.timeIn, name='clockIn'),
    path('clockOut/', views.timeOut, name='clockOut'),
    path('signUp/', views.signup, name='signUp'),
]