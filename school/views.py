from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'authentication/login.html')


from .models import Notification
def create_notification(user, message):
    if user.is_authenticated:
        Notification.objects.create(user=user, message=message)        # create notification object in the database
    

def dashboard(request):
    unread_notifications = Notification.objects.filter(user=request.user, is_read=False)
    context = {
        'unread_notifications': unread_notifications,
    }
    return render(request, 'student/student-dashboard.html', context)
