from rest_framework.serializers import ModelSerializer

from user_account.models import User


class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
