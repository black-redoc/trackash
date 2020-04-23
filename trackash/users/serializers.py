from django.conf import settings
from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    image_profile = Base64ImageField(required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "image_profile",
        )
        optional_fields = (
            "username",
            "email",
            "image_profile",
        )
