from django.contrib import admin
from main.models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(CourseContent)
admin.site.register(EnrollmentLog)