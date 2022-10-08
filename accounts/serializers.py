from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude =["password", "groups", "user_permissions"]



