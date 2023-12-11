from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.

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
    email = models.EmailField('email address', blank=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    theme_preference = models.CharField(max_length=20, choices=THEME_CHOICES, blank=True, null=True)
    language_preference = models.CharField('Language', max_length=20, choices=LANGUAGE_CHOICES, blank=True, null=True)


class Course(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    poster_url = models.FileField("Thumbnail", upload_to='posters/', default='posters/img2.png' )
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
    poster_url = models.FileField("Thumbnail", upload_to='posters/', default='posters/img2.png' )

    def __str__(self):
        return f"{self.course} - {self.title}"


class Lesson(models.Model):
    module = models.ForeignKey(CourseModule, on_delete=models.CASCADE,  db_constraint=False)
    title = models.CharField(max_length=255)
    video_url = models.FileField("Video", upload_to='videos/')
    poster_url = models.FileField("Thumbnail", upload_to='posters/')
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
