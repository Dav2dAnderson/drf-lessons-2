from django.contrib import admin

from .models import Service, Application, Notifications, Favourites
# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['owner', 'service', 'title', 'status']


@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ['user', 'sender', 'message']


@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_display = ['service', 'user', 'added_date']