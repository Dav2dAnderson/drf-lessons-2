from django.urls import path, include

from .views import ServiceViewSet, ApplicationViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('services', ServiceViewSet, basename='services')
router.register('my_applications', ApplicationViewSet, basename='my_applications')

urlpatterns = [
    path('', include(router.urls)),
]


