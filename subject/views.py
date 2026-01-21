from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Subject

@login_required(login_url='login')
def add_subject(request):
    if request.method == 'POST':
        code = request.POST.get('subject_code')
        name = request.POST.get('subject_name')
        class_level = request.POST.get('class_level')
        subject = Subject.objects.create(
            code=code,
            name=name,
            class_level=class_level
        )
        subject.save()
        messages.success(request, 'Subject added successfully!')
        return redirect('subject_list')
    
    return render(request, 'subject/add-subject.html')

@login_required(login_url='login')
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject/subject-list.html', {'subjects': subjects})

@login_required(login_url='login')
def edit_subject(request, code):
    subject = get_object_or_404(Subject, code=code)

    if request.method == 'POST':
        code = request.POST.get('subject_code')
        name = request.POST.get('subject_name')
        class_level = request.POST.get('class_level')
        
        subject.code = code
        subject.name = name
        subject.class_level = class_level
        subject.save()

        messages.success(request, 'Subject updated successfully!')
        # create_notification(request.user, f'Subject {subject.code} {subject.name} updated.')
        
        return redirect('subject_list')
    
    return render(request, 'subject/edit-subject.html', {'subject': subject})

@login_required(login_url='login')
def delete_subject(request, code):
    if request.method == 'POST':
        subject = get_object_or_404(Subject, code=code)
        subject_name = f'{subject.code} - {subject.name}'
        subject.delete()
        messages.success(request, f'{subject_name} deleted successfully!')
        return redirect('subject_list')
    return HttpResponseForbidden('Cannot delete subject')

