from dj_rest_auth.registration.serializers import RegisterSerializer

from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(required=True)

    _has_phone_field = True

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['phone_number'] = self.validated_data.get('phone_number', '')
        return data

