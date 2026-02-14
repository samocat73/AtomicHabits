from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from habit_tracker.models import Habit
from habit_tracker.services import send_telegram_message


@shared_task
def send_habit_reminder():
    today = timezone.now().date()
    habits = Habit.objects.all()
    for habit in habits:
        last_reminder_date = habit.last_reminder_date
        if last_reminder_date:
            next_reminder_date = last_reminder_date + timedelta(days=habit.periodicity)
        else:
            next_reminder_date = habit.created_at + timedelta(days=habit.periodicity)
        if next_reminder_date == today:
            send_telegram_message(
                habit.user.id_chat_tg,
                f"Сегодня в {habit.time} вам нужно {habit.action} в {habit.place}",
            )
            last_reminder_date = today
            habit.save()
