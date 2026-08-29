from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProfileModel(models.Model):
    images=models.ImageField(upload_to='uploads/',default='images/img.jpg')
    host=models.ForeignKey(User,on_delete=models.CASCADE)