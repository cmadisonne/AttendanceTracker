from django.contrib import admin

# Register your models here.
from .models import clockIn,clockOut

admin.site.register(clockIn)
admin.site.register(clockOut)