from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import attendanceModel
from .forms import attendanceForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    students = attendanceModel.objects.all()
    context = {'students': students}
    return render(request, 'attendanceApp/index.html', context)

def clockIn(request):
    return render(request, 'attendanceApp/')