from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Register(AbstractUser):
    class Meta:
        verbose_name = "Register"          
        verbose_name_plural = "Register"
    def __str__(self):
        return self.username
    
class Search_data(models.Model):
    Name=models.CharField()
    About=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
# Create your models here.
