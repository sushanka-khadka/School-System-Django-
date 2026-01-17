from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('<slug:slug>/', views.student_detail, name='student_detail'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<slug:slug>/', views.edit_student, name='edit_student'),
    path('delete/<slug:slug>/', views.delete_student, name='delete_student'),
]