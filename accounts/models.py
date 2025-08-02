from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomRole(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    role = models.ForeignKey(CustomRole, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
    

