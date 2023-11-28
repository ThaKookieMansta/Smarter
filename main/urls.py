from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
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
]