from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id_chat_tg = models.CharField(
        verbose_name="ID чата в telegram", help_text="Укажите ID чата в telegram"
    )
