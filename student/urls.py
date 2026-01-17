from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student-list'),
    path('add-student/', views.add_student, name='add-student'),
]