from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('mark-notification-as-read/<str:notification_id>/', views.mark_notification_as_read, name='mark_notification_as_read'),
    path('clear-all-notifications/', views.clear_notifications, name='clear_all_notifications'),
    path('show-all-notifications/', views.show_all_notifications, name='show_all_notifications'),
]