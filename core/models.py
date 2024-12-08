from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    """Represents a teacher."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    """Represents a student."""
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
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
    ]  # Ensure this list is properly closed

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    behavior_status = models.CharField(max_length=10, choices=BEHAVIOR_CHOICES)
    note = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.behavior_status}"
