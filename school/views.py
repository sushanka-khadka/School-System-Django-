from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Notification

def index(request):
    return render(request, 'authentication/login.html')


def create_notification(user, message):
    if user.is_authenticated:
        Notification.objects.create(user=user, message=message)        # create notification object in the database
    
@login_required(login_url='login')
def dashboard(request):
    unread_notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')
    context = {
        'notifications': unread_notifications,
    }
    return render(request, 'student/student-dashboard.html', context)

@login_required(login_url='login')
def mark_notification_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id, user=request.user)
    print('\n\nNotification ID:', notification_id)
    print('Notification Object:', notification)
    if request.method == 'POST' and notification:
        notification.is_read = True
        notification.save()     # mark as read
        
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

@login_required(login_url='login')
def clear_notifications(request):
    if request.method == 'POST':
        notifications = Notification.objects.filter(user=request.user)
        notifications.delete()
        return JsonResponse({'status': 'success'})
    return HttpResponseForbidden()

@login_required(login_url='login')
def show_all_notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'notifications': notifications,
    }
    return render(request, 'student/student-dashboard.html', context)