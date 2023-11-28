from django import template
from main.models import StudentCourse, UserProfile

register = template.Library()

@register.filter(name='is_enrolled')
def is_enrolled(student_profile, course):
    try:
        # Attempt to treat student_profile as a queryset
        return StudentCourse.objects.filter(student=student_profile, course=course).exists()
    except TypeError:
        # If it's not a queryset, assume it's a single object
        return StudentCourse.objects.filter(student=student_profile.user, course=course).exists()
