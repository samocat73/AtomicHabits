from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from habit_tracker.models import Habit
from habit_tracker.paginators import HabitPaginator
from habit_tracker.serializers import HabitSerializer
from user_account.permissions import IsOwner


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(Q(user=self.request.user) | Q(is_public=True))
