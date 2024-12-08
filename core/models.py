from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    """Represents a school."""
    name = models.CharField(max_length=100)
    end_of_school_time = models.TimeField(default="15:00")  # Default to 3:00 PM

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """Represents a teacher."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to User
    name = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)  # Optional school

    def __str__(self):
        return self.name


class Student(models.Model):
    """Represents a student."""
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    parent_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BehaviorLog(models.Model):
    """Logs a student's behavior."""
    BEHAVIOR_CHOICES = [
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('red', 'Red'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    behavior_status = models.CharField(max_length=10, choices=BEHAVIOR_CHOICES)
    note = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.behavior_status}"

