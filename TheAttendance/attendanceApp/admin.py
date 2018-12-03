from django.contrib import admin

# Register your models here.
from .models import attendanceModel

admin.site.register(attendanceModel)