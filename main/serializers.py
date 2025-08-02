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
        fields = ['id', 'owner', 'service']