from django.db import models

# Create your models here.
class Student(models.Model):
    'Student'
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    #TODO Look into how this works　：password　weqofihnn
    def __str__(self) -> str:
        return f"{self.name} {self.email}"

class Teacher(models.Model):
    'Teacher'
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
     #TODO Look into how this works　：password　weqofihnn
    
class Course(models.Model):
    'Course'
    name = models.CharField(max_length=50)
    Teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT)

class CourseContent(models.Model):
    'The content under a course like videos/text/quiz'
    Course = models.ForeignKey('Course', on_delete=models.CASCADE)

class EnrollmentLog(models.Model):
    'This stores the log of a student enrolling into a course'
    Student = models.ForeignKey('Student', on_delete=models.CASCADE)
    Course = models.ForeignKey('Course', on_delete=models.CASCADE)
