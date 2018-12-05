from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone

class attendanceModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    password = models.CharField(max_length=30)
    clockIn = models.DateTimeField(default=datetime.now)
    clockOut = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.username