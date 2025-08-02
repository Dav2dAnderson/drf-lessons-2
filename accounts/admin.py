from django.contrib import admin

from .models import CustomRole, CustomUser
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(CustomRole)

