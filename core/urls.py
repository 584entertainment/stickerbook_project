from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('log-behavior/', views.log_behavior, name='log_behavior'),  # Log behavior page
    path('student-summary/', views.student_summary, name='student_summary'),  # Student summary page
    path('add-student/', views.add_student, name='add_student'),  # Add student page
]

