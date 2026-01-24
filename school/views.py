from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Notification

from school import context_processors

@login_required(login_url='login')
def index(request):
    dashboards = context_processors.dashboards(request)['dashboards']

    if len(dashboards) >= 1:
     # multiples roles: render default at '/' and selected dashboard would be at dashboard/<role> URL
        dash = dashboards[0]['url_name']  # Default to first role
        if dash == 'admin_dashboard':
            return render(request, 'home/index.html', {'dashboards': dashboards})
        elif dash == 'teacher_dashboard':
            return render(request, 'teacher/teacher-dashboard.html', {'dashboards': dashboards})
        elif dash == 'student_dashboard':
            return render(request, 'student/student-dashboard.html', {'dashboards': dashboards})
    else:
        return redirect('login')  # No valid role found, redirect to login


def is_admin(user):
    return hasattr(user, 'is_admin') and user.is_admin
def is_teacher(user):
    return hasattr(user, 'is_teacher') and user.is_teacher
def is_student(user):
    return hasattr(user, 'is_student') and user.is_student

from student.models import Student
from department.models import Department

# protected views for each dashboard
@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def admin_dashboard(request):
    context = {
        'students': Student.objects.all(),
        'departments': Department.objects.all(),
    }
    return render(request, 'home/index.html', context)

@login_required(login_url='login')
@user_passes_test(is_teacher, login_url='login')
def teacher_dashboard(request):
    return render(request, 'teacher/teacher-dashboard.html')

@login_required(login_url='login')
@user_passes_test(is_student, login_url='login')
def student_dashboard(request):
    return render(request, 'student/student-dashboard.html')



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


#region notifications
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
#endregion

from home_auth.models import CustomUser
from school.forms import UserRoleForm

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def user_management(request):
    users = CustomUser.objects.all()
    context = {
        'users': users,
    }

    return render(request, 'home/user_management.html', context)