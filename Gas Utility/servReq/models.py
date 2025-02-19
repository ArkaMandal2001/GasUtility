import datetime
from django.db import models

# Create your models here.
class Request(models.Model):
    name=models.CharField(max_length=100)
    mobno=models.CharField(max_length=10)
    reqType=models.CharField(max_length=15)
    desc=models.TextField()
    dateTimeAdded=models.DateTimeField(default=datetime.datetime.now())
    dateTimeResolved=models.DateTimeField(default=datetime.datetime.now())
    status=models.CharField(max_length=15,default='Pending')