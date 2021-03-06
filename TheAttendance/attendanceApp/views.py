from django.shortcuts import render, redirect, get_object_or_404
from .models import clockOut, clockIn
from .forms import clockInForm, clockOutForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth import logout
from django.contrib import messages


@login_required
def index(request):
    clockInRecord = clockIn.objects.filter(username=request.user)
    clockOutRecord = clockOut.objects.filter(username=request.user)
    context = {'clockInRecord': clockInRecord, 'clockOutRecord': clockOutRecord}
    return render(request, 'attendanceApp/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
        return render(request, 'attendanceApp/signUp.html', {'form': form})

def timeIn(request):
    if request.method == 'POST':
        form = clockInForm(request.POST)
        if form.is_valid():
            form.username = request.user
            form.password = form.cleaned_data['password']
            form.clockIn = form.cleaned_data['clockIn']
            form.save()
            messages.success(request, 'You have successfully PLUGGED  IN')
            return redirect('clock')
    else:
        form = clockInForm()
        return render(request, 'attendanceApp/clockIn.html', {'form':form})

def timeOut(request):
    if request.method == 'POST':
        form = clockOutForm(request.POST)
        if form.is_valid():
            form.username = request.user
            form.password = form.cleaned_data['password']
            form.clockOut = form.cleaned_data['clockOut']
            form.save()
            messages.success(request, 'You have successfully PLUGGED  OUT')
            return redirect('clock')
    else:
        form = clockOutForm()
        return render(request, 'attendanceApp/clockOut.html', {'form':form})

def base (request):
    return render(request, 'attendanceApp/base.html')

