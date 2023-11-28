import django_filters
from .models import Course
from django import forms


class CourseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Search Courses'
    )

    class Meta:
        model = Course
        fields = ['title', ]
