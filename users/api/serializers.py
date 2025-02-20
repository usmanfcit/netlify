from datetime import datetime, timezone

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "is_active",
            "is_staff"
        ]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        exp_timestamp = self.get_token(self.user)["exp"]
        exp_time = datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)
        expiry_time = exp_time.isoformat()
        user_data_serialized = UserSerializer(self.user)
        user_data = user_data_serialized.data
        user_data["exp"] = expiry_time
        user_data["access"] = data["access"]
        user_data["refresh"] = data["refresh"]
        return user_data


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "password", "email", "phone_number")

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user