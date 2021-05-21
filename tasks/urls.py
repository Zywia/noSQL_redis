from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, CashTaskViewSet

router = DefaultRouter()
router.register(r'task', TaskViewSet, basename="task")
router.register(r'cache_task', CashTaskViewSet, basename="cache_task")


urlpatterns = [
    path('', include(router.urls)),
]
