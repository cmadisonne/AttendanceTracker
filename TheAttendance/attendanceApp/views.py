from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import attendanceModel
from .forms import attendanceForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
#     Landing Page for user to log in or sign-up

