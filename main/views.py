import os
import time
from wsgiref.util import FileWrapper

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import default_storage
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from formtools.wizard.views import SessionWizardView

from main.forms import SignUpForm, CourseForm, ModuleForm, LessonForm
from main.models import Lesson, Course, CourseModule, UserProfile, StudentCourse
from .filters import CourseFilter


# Create your views here.


def index(request):
    """
    This view handles the homepage of the web app
    Args:
        request:

    Returns: The homepage

    """
    courses = Course.objects.all().order_by('-id')
    return render(request, 'main/index.html', {
        "courses": courses[:3],
        "logstat": request.user,
    })


def user_login(request):
    if request.method == "GET":
        signin_form = AuthenticationForm()
        return render(request, 'main/sign-up.html', {
            "form": signin_form
        })

    if request.method == "POST":

        signin_form = AuthenticationForm(request, data=request.POST)

        if signin_form.is_valid():

            user = authenticate(request, username=signin_form.cleaned_data['username'],
                                password=signin_form.cleaned_data['password'])

            if user is not None:
                login(request, user)

                # Redirect to a success page
                return redirect('check-role')
            else:
                return render(request, 'main/sign-up.html', {
                    "form": signin_form, })
        else:
            form = AuthenticationForm(request)


def signup(request):
    if request.method == "GET":
        signup_form = SignUpForm()
        return render(request, 'main/sign-up.html', {
            "form": signup_form
        })

    if request.method == "POST":
        signup_form = SignUpForm(request.POST, request.FILES)

        if signup_form.is_valid():
            signup_form.save()
            return redirect('home')


def redirect_based_on_role(request):
    user_profile = UserProfile.objects.get(username=request.user)

    if user_profile.role == 1:  # Student
        return redirect('student_view')
    elif user_profile.role == 2:  # Instructor
        return redirect('instructor_view')
    else:
        # Handle other roles or scenarios
        return redirect('home')


@login_required
def student_view(request):
    # Assuming you have a ForeignKey relationship between UserProfile and User
    user_profile = UserProfile.objects.get(username=request.user)
    return redirect('courses')


@login_required
def instructor_view(request):
    # Assuming you have a ForeignKey relationship between UserProfile and User
    user_profile = UserProfile.objects.get(username=request.user)
    return redirect('instructor-courses')


# def is_student_enrolled(student_profile, course):
#     return StudentCourse.objects.filter(student=student_profile, course=course).exists()


@login_required
def student_courses(request):
    courses = Course.objects.all()
    student_profile = UserProfile.objects.get(username=request.user)
    course_filter = CourseFilter(request.GET, queryset=courses)
    courses = course_filter.qs

    return render(request, 'main/student-courses.html', {
        "courses": courses,
        "logstat": request.user,
        "student_profile": student_profile,
        "course_filter": course_filter
    })


def instructor_courses(request):
    instructor = UserProfile.objects.get(username=request.user)
    courses = Course.objects.filter(instructor=instructor.id)

    context = {
        "courses": courses,
        "logstat": request.user,
    }

    if request.method == 'GET':
        course_form = CourseForm(initial={'instructor': instructor})
        context['course_form'] = course_form
        return render(request, 'main/instructor-courses.html', context)

    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)

        module_form = ModuleForm(request.POST, request.FILES)
        if course_form.is_valid():
            # Set the instructor before saving
            course = course_form.save(commit=False)
            course.instructor = instructor
            course.save()
            messages.success(request, 'New Course Added')
            return redirect('instructor-courses')

    return render(request, 'main/instructor-courses.html', context)


def instructor_modules(request, id):

    course = Course.objects.get(id=id)
    modules = CourseModule.objects.filter(course=course)
    context = {
        "modules": modules,
        "course": course.title,
        "logstat": request.user,
    }

    module_form = ModuleForm()
    context['module_form'] = module_form

    if request.method == 'GET':
        module_form = ModuleForm()
        context['module_form'] = module_form
        return render(request, 'main/instructor-modules.html', context)

    if request.method == 'POST':
        module_form = ModuleForm(request.POST, request.FILES)
        if module_form.is_valid():
            module = module_form.save(commit=False)
            module.course_id = course.id
            module.save()
            messages.success(request, 'New Module Added')
            return render(request, 'main/instructor-modules.html', context)

    return render(request, 'main/instructor-modules.html', context)

def instructor_lesson(request, id):
    module = CourseModule.objects.get(id=id)
    lessons = Lesson.objects.filter(module=module)


    context = {
        "lessons": lessons,
        "logstat": request.user,
        "module": module.title,
    }
    lesson_form = LessonForm()
    context['lesson_form'] = lesson_form

    if request.method == 'GET':
        lesson_form = LessonForm()
        context['lesson_form'] = lesson_form
        return render(request, 'main/instructor-lessons.html', context)

    if request.method == 'POST':
        lesson_form = LessonForm(request.POST, request.FILES)
        if lesson_form.is_valid():
            lesson = lesson_form.save(commit=False)
            lesson.module_id = module.id
            lesson.save()
            messages.success(request, 'New Lesson Added')
            return render(request, 'main/instructor-lessons.html', context)

    return render(request, 'main/instructor-lessons.html', )


@login_required
def modules(request, id):
    course = Course.objects.get(id=id)
    modules = CourseModule.objects.filter(course=course)
    return render(request, 'main/course.html', {
        "modules": modules,
        "course": course.title,
        "logstat": request.user,
    })


@login_required
def lessons(request, id):
    module = CourseModule.objects.get(id=id)
    lessons = Lesson.objects.filter(module=module)
    return render(request, 'main/lessons.html', {
        "lessons": lessons,
        "logstat": request.user,
    })


@login_required
def lesson(request, id):
    lesson = Lesson.objects.get(id=id)
    all_lessons = lesson.get_all_lessons_in_module()
    courses = Course.objects.all().order_by('-id')


    return render(request, 'main/lesson.html', {
        "lesson": lesson,
        "list": all_lessons,
        "logstat": request.user,
        "courses": courses[:3]
    })


def student_enroll(request, id):
    course_to_enroll = Course.objects.get(id=id)
    student = UserProfile.objects.get(username=request.user)
    course_enrolled, created = StudentCourse.objects.get_or_create(student=student)
    course_enrolled.course.add(course_to_enroll)
    modules = CourseModule.objects.filter(course=course_to_enroll)
    return render(request, 'main/course.html', {
        "modules": modules,
        "course": course_to_enroll.title,
        "logstat": request.user,
    })

# Instructor content form wizard
