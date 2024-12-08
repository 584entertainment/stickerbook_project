from django import forms
from .models import BehaviorLog, Student, School

class BehaviorLogForm(forms.ModelForm):
    class Meta:
        model = BehaviorLog
        fields = ['student', 'behavior_status', 'note']
        widgets = {
            'note': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name']  # Include fields that exist in your Student model

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'end_of_school_time']  # Fields to be configured for each school

