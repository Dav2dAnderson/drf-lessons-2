from django.db import models
from django.utils.text import slugify

from accounts.models import CustomUser
# Create your models here.


# Xizmatlar
class Service(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


# Ariza
class Application(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Kutilyabdi'),
        ('reviewed', "Ko'rib chiqildi")
    )
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return self.owner.username

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = "Applications"


# Habarlar 
class Notifications(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='notifications')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='my_notifications')
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = "Notifications"