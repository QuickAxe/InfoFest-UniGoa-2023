from django.db import models 
# Create your models here.
class Student(models.Model):
    'Student'
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50, default="password")
    def __str__(self) -> str:
        return f"{self.name}"

class Teacher(models.Model):
    'Teacher'
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length=50, default="password")
    def __str__(self) -> str:
        return f"{self.name}"
 
class Course(models.Model):
    'Course'
    name = models.CharField(max_length=50)
    # TeacherName = models.CharField(max_length=50)
    Teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.name}"


class CourseContent(models.Model):
    'The content under a course like videos/text/quiz'
    Course = models.ForeignKey('Course', on_delete=models.CASCADE)
    videoURL = models.URLField(max_length=200, default='example.com')
    textContent = models.CharField(max_length=500, default="lorem ipsum dolor set")
    # def __str__(self) -> str:
    #     return f"{self.textContent} mmm"

class EnrollmentLog(models.Model):
    'This stores the log of a student enrolling into a course'
    Student = models.ForeignKey('Student', on_delete=models.CASCADE)
    Course = models.ForeignKey('Course', on_delete=models.CASCADE)
    progress = models.IntegerField(default = 0)
    def __str__(self) -> str:
        return f"{self.Student.name} {self.Course}"

class Question(models.Model):
    "This is a question in a particular forum (for the Course which is a Foreign Key)"
    Course = models.ForeignKey('Course', on_delete=models.CASCADE)
    Student = models.ForeignKey('Student', on_delete=models.CASCADE, default=1)
    textContent = models.CharField(max_length=500)
    dateAndTimePosted = models.DateTimeField(auto_now_add=True)
    isAnswered = models.BooleanField(default=False)
    def __str__(self)->str:
        return f'{self.textContent}'


class Answer(models.Model):
    'This is the answer on a particular question'
    Question =  models.ForeignKey('Question', on_delete=models.CASCADE)
    Student = models.ForeignKey('Student', on_delete=models.CASCADE,  default=1)
    textContent = models.CharField(max_length=500)
    dateAndTimePosted = models.DateTimeField(auto_now_add=True)
    netVotes = models.IntegerField(default=0)
    def __str__(self)->str:
        return f'{self.textContent}'

# class Reply(models.Model):
#     Answer =  models.ForeignKey('Answer', on_delete=models.CASCADE)
#     textContent = models.CharField(max_length=500)
#     dateAndTimePosted = models.DateTimeField(auto_now_add=True)
#     netVotes = models.IntegerField(default=0)

class VoteLog(models.Model):
    'VoteLog keeps track of every Vote.'
    Student = models.ForeignKey('Student', on_delete=models.CASCADE)
    Answer = models.ForeignKey('Answer', on_delete=models.CASCADE)
    def __str__(self)->str:
        return f'{self.Student.name} : {self.Answer.textContent}'
    



class QuizContent(models.Model):

    quiz = models.ForeignKey('Course', on_delete=models.CASCADE)
    
    q1 = models.CharField(max_length=100)

#-----------------------------------------------------
    q1A = models.CharField(max_length=100)
    q1B = models.CharField(max_length=100)
    q1C = models.CharField(max_length=100)
    q1D = models.CharField(max_length=100)
#-----------------------------------------------------
    correctAns = models.IntegerField(default=3)



# class Quiz(models.Module):
     
#     course = models.ForeignKey('Course', on_delete=models.CASCADE)
#     q1 = models.CharField(max_length=100)
#     q2 = models.CharField(max_length=100)
#     q3 = models.CharField(max_length=100)
#     q4 = models.CharField(max_length=100)
#     q5 = models.CharField(max_length=100)