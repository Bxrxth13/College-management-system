from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Enrollment
from django.contrib import messages  # Import messages framework for feedback
from django.db import IntegrityError  # Import IntegrityError to handle unique constraints

def home(request):
    return render(request, 'college/home.html')  # Create a home.html template

# Student Views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'college/student_list.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        email = request.POST.get('email')
        age = request.POST.get('age')

        try:
            student = Student(name=name, roll_number=roll_number, email=email, age=age)
            student.save()
            messages.success(request, 'Student added successfully.')
            return redirect('student_list')
        except IntegrityError:
            messages.error(request, 'Roll number or email must be unique.')

    return render(request, 'college/add_student.html')

def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.roll_number = request.POST.get('roll_number')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')

        try:
            student.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('student_list')
        except IntegrityError:
            messages.error(request, 'Roll number or email must be unique.')

    return render(request, 'college/edit_student.html', {'student': student})

def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    messages.success(request, 'Student deleted successfully.')
    return redirect('student_list')

# Course Views
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'college/course_list.html', {'courses': courses})

def add_course(request):
    if request.method == "POST":
        title = request.POST.get('title')
        code = request.POST.get('code')
        description = request.POST.get('description')

        try:
            Course.objects.create(title=title, code=code, description=description)
            messages.success(request, 'Course added successfully.')
            return redirect('course_list')
        except IntegrityError:
            messages.error(request, 'Course code must be unique.')

    return render(request, 'college/add_course.html')

def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == "POST":
        course.title = request.POST.get('title')
        course.code = request.POST.get('code')
        course.description = request.POST.get('description')

        try:
            course.save()
            messages.success(request, 'Course updated successfully.')
            return redirect('course_list')
        except IntegrityError:
            messages.error(request, 'Course code must be unique.')

    return render(request, 'college/edit_course.html', {'course': course})

def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    messages.success(request, 'Course deleted successfully.')
    return redirect('course_list')

# Enrollment Views
def enroll_student(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        course_id = request.POST.get('course_id')

        try:
            Enrollment.objects.create(student_id=student_id, course_id=course_id)
            messages.success(request, 'Student enrolled successfully.')
            return redirect('student_list')  # Redirect after enrollment
        except IntegrityError:
            messages.error(request, 'Student is already enrolled in this course.')

    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'college/enroll_student.html', {'students': students, 'courses': courses})
