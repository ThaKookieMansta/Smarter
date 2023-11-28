from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.

# class UserProfile(models.Model):
#     ROLE_CHOICES = [
#         ("Instructor", "Instructor"),
#         ("Student", "Student"),
#         ("Admin", "Admin"),
#     ]
#
#     THEME_CHOICES = [
#         ("Dark Mode", "Dark"),
#         ("light Mode", "Light"),
#         ("System Default", "System")
#     ]
#
#     LANGUAGE_CHOICES = [
#         ("English", "en"),
#     ]
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#     facebook_url = models.URLField(blank=True, null=True)
#     twitter_url = models.URLField(blank=True, null=True)
#     linkedin_url = models.URLField(blank=True, null=True)
#     theme_preference = models.CharField(max_length=20, choices=THEME_CHOICES, blank=True, null=True)
#     language_preference = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, blank=True, null=True)


class UserProfile(AbstractUser):
    ROLE_CHOICES = [
        (1, "Student"),
        (2, "Instructor"),
    ]

    THEME_CHOICES = [
        ("Dark Mode", "Dark"),
        ("light Mode", "Light"),
        ("System Default", "System")
    ]
    LANGUAGE_CHOICES = [
        ("English", "en"),
    ]

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True)
    theme_preference = models.CharField(max_length=20, choices=THEME_CHOICES, blank=True, null=True)
    language_preference = models.CharField('Language', max_length=20, choices=LANGUAGE_CHOICES, blank=True, null=True)


class Course(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    poster_url = models.FileField(upload_to='posters/', default='posters/img2.png' )
    instructor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, db_constraint=False)

    # slug = models.SlugField(max_length=500, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.instructor} - {self.title}"



class StudentCourse(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)


class InstructorCourse(models.Model):
    instructor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)


class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,  db_constraint=False)
    title = models.CharField(max_length=255)
    poster_url = models.FileField(upload_to='posters/', default='posters/img2.png' )

    def __str__(self):
        return f"{self.course} - {self.title}"


class Lesson(models.Model):
    module = models.ForeignKey(CourseModule, on_delete=models.CASCADE,  db_constraint=False)
    title = models.CharField(max_length=255)
    video_url = models.FileField(upload_to='videos/')
    poster_url = models.FileField(upload_to='posters/')
    instructor_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    def get_all_lessons_in_module(self):
        """
        Retrieve all lessons in the same module as the current lesson.
        """
        return Lesson.objects.filter(module=self.module)


class StudentProgress(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)
