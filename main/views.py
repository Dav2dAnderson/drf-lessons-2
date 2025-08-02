from django.shortcuts import render

from rest_framework import viewsets, generics, permissions

from .models import Service, Application, Notifications
from .serializers import ServicesListSerializer, ServicesRetrieveSerializer, ApplicationsSerializer
# Create your views here.

# POST, PUT, DELETE, GET = CREATE, UPDATE, DELETE, RETRIEVE, GET
class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServicesListSerializer
    lookup_field = 'slug'


class ApplicationAPIView(generics.ListCreateAPIView, generics.RetrieveUpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationsSerializer
