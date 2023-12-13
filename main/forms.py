"""
Forms for the Smarter main application
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from main.models import Course, StudentCourse, UserProfile, InstructorCourse, CourseModule, Lesson


class SignUpForm(UserCreationForm):
    """
    This class creates the form for the user creation model
    """
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = ["username", "first_name", "last_name", "email", "language_preference", "role"]

# Instructor Form for uploading content
class CourseForm(forms.ModelForm):
    """
        This class creates the form for the course model
        """
    class Meta:
        model = Course
        fields = ['title', 'description', 'poster_url']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         'title',
    #         'description',
    #         Submit('submit', 'Next', css_class='btn btn-primary')
    #     )

class ModuleForm(forms.ModelForm):
    """
        This class creates the form for the module model
        """
    class Meta:
        model = CourseModule
        fields = ['title', 'poster_url']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         'title',
    #         Submit('submit', 'Next', css_class='btn btn-primary')
    #     )

class LessonForm(forms.ModelForm):
    """
        This class creates the form for the Lesson model
        """
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'poster_url', 'instructor_notes']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         'title',
    #         'video_url',
    #         'poster_url',
    #         'instructor_notes',
    #         Submit('submit', 'Finish', css_class='btn btn-primary')
    #     )
