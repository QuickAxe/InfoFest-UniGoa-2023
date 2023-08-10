from django.urls import path
from . import views 

urlpatterns = [
    path('getCourse/', views.getCourse),
    path('get/', views.getCourse)
]
