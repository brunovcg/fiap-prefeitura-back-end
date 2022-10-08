from rest_framework import serializers
from .models import Buildings
from accounts.serializers import UserSerializer

class BuildingsSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Buildings
        fields = "__all__"

