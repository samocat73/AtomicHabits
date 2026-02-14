from django.core.validators import MaxValueValidator
from django.db import models

from user_account.models import User


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )
    place = models.CharField(
        max_length=120,
        verbose_name="Место выполнения привычки",
        help_text="Укажите место выполнения привычки",
    )
    time = models.TimeField(
        help_text="Укажите время, в которое будет выполняться привычка",
        verbose_name="Время выполнения привычки",
    )
    action = models.CharField(
        max_length=120,
        verbose_name="Действие",
        help_text="Укажите действие, которое выполняется в качестве привычки",
    )
    is_pleasant = models.BooleanField(
        help_text="Укажите признак приятной привычки",
        verbose_name="Признак приятной привычки",
        default=False,
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Укажите связанную привычку",
        verbose_name="Связанная привычка",
    )
    periodicity = models.PositiveIntegerField(
        default=1,
        validators=[MaxValueValidator(7)],
        verbose_name="Периодичность",
        help_text="Укажите периодичность выполнения привычки",
    )
    award = models.TextField(
        blank=True,
        null=True,
        verbose_name="Вознаграждение",
        help_text="Укажите вознаграждение",
    )
    time_to_complete = models.PositiveIntegerField(
        validators=[MaxValueValidator(120)],
        verbose_name="Время выполнения привычки",
        help_text="Укажите время выполнения привычки",
    )
    is_public = models.BooleanField(
        default=True,
        verbose_name="Признак публичной привычки",
        help_text="Укажите признак публичной привычки",
    )
    last_reminder_date = models.DateField(
        default=None, null=True, blank=True, verbose_name="Дата последнего напоминания"
    )
    created_at = models.DateField(
        auto_now_add=True, verbose_name="Дата создания привычки"
    )
