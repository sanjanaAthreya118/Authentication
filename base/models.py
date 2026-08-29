from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskModel(models.Model):
    title=models.CharField(max_length=30)
    desc=models.CharField(max_length=30)
    is_delete=models.BooleanField(default=False)
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.IntegerField()