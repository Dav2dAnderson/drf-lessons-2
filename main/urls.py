from django.urls import path, include

from .views import ServiceViewSet, ApplicationAPIView

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('services', ServiceViewSet, basename='services')


urlpatterns = [
    path('', include(router.urls)),
    path('applications/', ApplicationAPIView.as_view())
]
