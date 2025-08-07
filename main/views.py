from django.shortcuts import render

from rest_framework import viewsets, generics, permissions, filters

from .models import Service, Application, Notifications
from .serializers import ServicesListSerializer, ServicesRetrieveSerializer, ApplicationsSerializer, ApplicationDetailSerializer
# Create your views here.

# POST, PUT, DELETE, GET = CREATE, UPDATE, DELETE, RETRIEVE, GET
class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServicesListSerializer
    lookup_field = 'slug'

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class ApplicationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Application.objects.all()
    serializer_class = ApplicationsSerializer
    lookup_field = 'slug'

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'status']
   
    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'list':
            return ApplicationsSerializer
        return ApplicationDetailSerializer
    
    def get_queryset(self):
        return Application.objects.filter(owner=self.request.user)

