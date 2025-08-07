from rest_framework import serializers

from .models import Service, Application, Notifications


class ServicesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'slug']


class ServicesRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description']


class ApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'owner', 'service', 'title', 'slug', 'description', 'created_date']


class ApplicationDetailSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source='owner.username', read_only=True) # owner_username = 'admin'
    service_title = serializers.CharField(source='service.title', read_only=True)
    class Meta:
        model = Application
        fields = [
            'id', 'owner', 'owner_username', 'service', 'service_title', 'title', 'description', 'status', 'created_date', 'updated_date'
            ]