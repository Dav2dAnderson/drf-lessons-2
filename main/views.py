from django.shortcuts import render

from rest_framework import viewsets, generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Service, Application, Notifications, Favourites
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

    @action(detail=True, methods=['post'], url_path='add_favourites', url_name='add_favourites')
    def add_favourites(self, request, *args, **kwargs):
        user = self.request.user
        service = self.get_object()
        if not Favourites.objects.filter(user=user, service=service).exists():
            favourites = Favourites.objects.create(user=user, service=service)
            if favourites:
                return Response({"detail": "Created"}, status=status.HTTP_201_CREATED)
        return Response({'detail': "Already exists"}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['delete'], url_path='delete_favourites', url_name='delete_favourites')
    def delete_favourites(self, request, *args, **kwargs):
        user = self.request.user
        service = self.get_object()
        if Favourites.objects.filter(user=user, service=service).exists():
            favourites = Favourites.objects.filter(user=user, service=service).delete()
            if favourites:
                return Response({'detail': 'Deleted'}, status=status.HTTP_200_OK)
        return Response({'detail': "Doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)


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

