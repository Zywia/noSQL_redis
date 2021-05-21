from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CashTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @method_decorator(cache_page(60 * 60))
    def dispatch(self, *args, **kwargs):
        return super(CashTaskViewSet, self).dispatch(*args, **kwargs)
