"""
URL configuration for smarter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView)
from django.urls import path, include

from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('student-courses/', views.student_courses, name='courses'),
    path('course/<int:id>/', views.modules, name='course'),
    path('module/<int:id>/', views.lessons, name='lessons'),
    path('lesson/<int:id>/', views.lesson, name='lesson'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.user_login, name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('check-role/', views.redirect_based_on_role, name='check-role'),
    path('student/', views.student_view, name='student_view'),
    path('instructor/', views.instructor_view, name='instructor_view'),
    path('enroll/<int:id>/', views.student_enroll, name='enroll'),
    path('instructor-courses/',views.instructor_courses, name='instructor-courses'),
    path('instructor-modules/<int:id>/', views.instructor_modules, name='instructor-modules'),
    path('instructor-lessons/<int:id>/', views.instructor_lesson, name='instructor-lessons'),
    path('reset_password/', PasswordResetView.as_view(template_name="main/password_reset.html"), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"), name='password_reset_complete'),

]