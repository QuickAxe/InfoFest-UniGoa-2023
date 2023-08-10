from django.urls import path
from . import views 

urlpatterns = [
    path('getCourse/', views.getCourse),
    path('addCourse/', views.addCourse),
    path('addCourseContent/', views.addCourseContent),
    path('getStudentCourse/', views.getStudentCourse),
    
]
