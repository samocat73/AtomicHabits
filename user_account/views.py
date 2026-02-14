from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from user_account.serializers import UserRegistrationSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
