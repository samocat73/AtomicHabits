from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from user_account.apps import UserAccountConfig
from user_account.views import UserCreateAPIView

app_name = UserAccountConfig.name

urlpatterns = [
    path("api/register/", UserCreateAPIView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
