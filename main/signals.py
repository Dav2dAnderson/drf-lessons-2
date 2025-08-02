from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Service, Notifications, Application
from accounts.models import CustomUser

# 1-signal: Service qo'shilganligi haqida habar
@receiver(post_save, sender=Service)
def notify_about_service_changes(sender, instance, created, **kwargs):
    if created:
        print("==============\nYangi xizmat qo'shildi, iltimos tanishib chiqing\n==============")
        
        message = "Yangi xizmat qo'shildi, iltimos tanishib chiqing"
        Notifications.objects.create(
            sender=CustomUser.objects.get(pk=1), user=CustomUser.objects.get(pk=2), message=message
        )


# 2-signal: Service o'chirilganligi haqida habar
@receiver(post_delete, sender=Service)
def notify_about_service_deletion(sender, instance, **kwargs):
    print("==============\nXizmat o'chirildi.\n==============")

    message = "Xizmat o'chirildi."
    Notifications.objects.create(
        sender=CustomUser.objects.get(username='admin'), user=CustomUser.objects.get(pk=2), message=message
    )
# post_save = create, post_delete = remove

@receiver(post_save, sender=Application)
def notify_about_application_changes(sender, instance, created, **kwargs):
    if not created:
        message = "Arizangiz qabul qilindi."
        Notifications.objects.create(
            sender=CustomUser.objects.get(username='admin'), user=instance.owner, message=message
        )
    else:
        message = "Ariza qo'shildi."
        Notifications.objects.create(
            sender=CustomUser.objects.get(username='admin'), user=instance.owner, message=message
        )

