import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    created_at__date = django_filters.DateFilter(field_name='created_at', lookup_expr='date')
    status = django_filters.BooleanFilter(field_name='status')

    class Meta:
        model = Task
        fields = ['created_at__date', 'status']
