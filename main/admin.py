from django.contrib import admin
from main.models import User, StudentCourse, UserProfile, StudentProgress, CourseModule, Course, Lesson, \
    InstructorCourse


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "instructor")

class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "module")

# admin.site.register(User)
admin.site.register(StudentCourse)
admin.site.register(UserProfile)
admin.site.register(StudentProgress)
admin.site.register(CourseModule)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(InstructorCourse)
