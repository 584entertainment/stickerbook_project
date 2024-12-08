from django.shortcuts import render, redirect
from .models import Student, BehaviorLog
from .forms import BehaviorLogForm, StudentForm

def log_behavior(request):
    """Page for logging student behavior."""
    if request.method == 'POST':
        # Process the submitted form data
        form = BehaviorLogForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('log_behavior')  # Redirect to the same page after submission
    else:
        # Display an empty form for GET requests
        form = BehaviorLogForm()

    # Retrieve all students to display on the page
    students = Student.objects.all()
    return render(request, 'core/log_behavior.html', {'form': form, 'students': students})

def student_summary(request):
    """Page for viewing a student's behavior summary."""
    # Fetch all students for the dropdown
    students = Student.objects.all()

    # Get the selected student ID from the query parameters
    selected_student = request.GET.get('student') or ""  # Default to an empty string

    # Filter logs by the selected student, or show all logs
    if selected_student:
        behavior_logs = BehaviorLog.objects.filter(student_id=selected_student)
    else:
        behavior_logs = BehaviorLog.objects.all()

    # Pass the context to the template
    context = {
        'logs': behavior_logs,
        'students': students,
        'selected_student': selected_student,  # Pass the selected student ID as a string
    }
    return render(request, 'core/student_summary.html', context)

def home(request):
    """Home page for teachers or parents."""
    return render(request, 'core/home.html')

def add_student(request):
    """Page for adding a new student."""
    if request.method == 'POST':
        # Process the submitted form data
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new student to the database
            return redirect('add_student')  # Redirect to the same page after submission
    else:
        # Display an empty form for GET requests
        form = StudentForm()

    return render(request, 'core/add_student.html', {'form': form})

