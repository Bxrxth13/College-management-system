from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)  # Unique roll number
    email = models.EmailField(unique=True)  # Adding uniqueness to email for data integrity
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)  # Unique code for each course
    description = models.TextField()

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'course')  # Ensure a student can't enroll in the same course twice

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.title}"
