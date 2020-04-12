from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
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