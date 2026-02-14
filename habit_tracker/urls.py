from rest_framework import routers

from habit_tracker.apps import HabitTrackerConfig
from habit_tracker.views import HabitViewSet

router = routers.DefaultRouter()
router.register("", HabitViewSet)
app_name = HabitTrackerConfig.name

urlpatterns = []
urlpatterns += router.urls
