from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Register(AbstractUser):
    class Meta:
        verbose_name = "Register"          
        verbose_name_plural = "Register"
    ROLE_CHOICES=(
        ('admin','Admin'),
        ('user',"User"),
    )
    Role=models.CharField(choices=ROLE_CHOICES,default='user')
    def __str__(self):
        return self.username
    

class Booking(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField()
    date=models.DateField()
    time=models.TimeField()
    is_booked=models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name}-{self.date}"

# Create your models here.
