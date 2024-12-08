from datetime import datetime, timedelta
from django.utils.timezone import now
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Student, BehaviorLog, Teacher
from .forms import BehaviorLogForm, StudentForm

def home(request):
    """Home page for teachers or parents."""
    return render(request, 'core/home.html')


def log_behavior(request):
    """Page for logging student behavior."""
    if request.user.is_authenticated:
        try:
            teacher = Teacher.objects.get(user=request.user)
            end_of_school_time = teacher.school.end_of_school_time
        except Teacher.DoesNotExist:
            messages.error(request, "You are not associated with a school.")
            return redirect('home')  # Redirect if teacher record not found
    else:
        messages.error(request, "You must be logged in to access this page.")
        return redirect('login')  # Redirect to login if not authenticated

    # Calculate the cutoff time (1 hour after end_of_school_time)
    CUTOFF_TIME = (datetime.combine(now().date(), end_of_school_time) + timedelta(hours=1)).time()
    current_time = now().time()

    if current_time > CUTOFF_TIME:
        messages.error(request, "Behavior logging is closed for today.")
        return redirect('home')  # Redirect to home or appropriate page

    if request.method == 'POST':
        form = BehaviorLogForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, "Behavior log saved successfully.")
            return redirect('log_behavior')  # Redirect after submission
    else:
        form = BehaviorLogForm()

    # Retrieve students associated with the logged-in teacher
    students = Student.objects.filter(teacher=teacher)
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
        'selected_student': selected_student,
    }
    return render(request, 'core/student_summary.html', context)


def add_student(request):
    """Page for adding a new student."""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)  # Get the student instance but don't save yet
            if not student.teacher:  # Check if a teacher is not assigned
                default_teacher = Teacher.objects.get(user__username="default_teacher")
                student.teacher = default_teacher  # Assign the default teacher
            student.save()  # Save the student with the assigned teacher
            messages.success(request, "Student added successfully.")
            return redirect('add_student')  # Redirect to refresh the page
    else:
        form = StudentForm()

    return render(request, 'core/add_student.html', {'form': form})
