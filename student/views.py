from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseForbidden
# Create your views here.
from .models import Student, Parent

def add_student(request):
    if request.method == 'POST':
        # retrieve student data from the form
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_class = request.POST.get('student_class')
        section = request.POST.get('section')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        religion = request.POST.get('religion')
        admission_number = request.POST.get('admission_number')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        student_image = request.FILES.get('student_image')     # must use request.FILES to get file data
        # parent = request.POST.get('parent')       # false, we will create parent object separately (one to one relationship)
        # slug = request.POST.get('slug')

        # retrieve parent data from the form
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

        # save the student and parent data to the database
        parent = Parent.objects.create(
                    father_name=father_name,
                    father_occupation=father_occupation,
                    father_mobile=father_mobile,
                    father_email=father_email,
                    mother_name=mother_name,
                    mother_occupation=mother_occupation,
                    mother_mobile=mother_mobile,
                    mother_email=mother_email,
                    present_address=present_address,
                    permanent_address=permanent_address
                )

        # save student data
        Student.objects.create(
            student_id=student_id,
            first_name=first_name,
            last_name=last_name,
            student_class=student_class,
            section=section,
            gender = gender,
            date_of_birth = date_of_birth,
            religion = religion,
            admission_number = admission_number,
            joining_date = joining_date,
            mobile_number = mobile_number,
            student_image = student_image,
            parent = parent,            
        )

        messages.success(request, 'Student added successfully!')
        return redirect('student-list')
    
    return render(request, 'student/add-student.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student-list.html', {'students': students})

def student_detail(request, slug):
    student = get_object_or_404(Student, slug=slug)
    return render(request, 'student/student-detail.html', {'student': student})

def edit_student(request, slug):
    student = get_object_or_404(Student, slug=slug)     # automatically returns 404 if not found
    parent = student.parent if hasattr(student, 'parent') else None # get the related parent object else None

    if request.method == 'POST':
        # retrieve student data from the form
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_class = request.POST.get('student_class')
        section = request.POST.get('section')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        religion = request.POST.get('religion')
        admission_number = request.POST.get('admission_number')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        student_image = request.FILES.get('student_image') if request.FILES.get('student_image') else student.student_image

        # retrieve parent data from the form
        parent.father_name = request.POST.get('father_name')
        parent.father_occupation = request.POST.get('father_occupation')
        parent.father_mobile = request.POST.get('father_mobile')
        parent.father_email = request.POST.get('father_email')
        
        parent.mother_name = request.POST.get('mother_name')
        parent.mother_occupation = request.POST.get('mother_occupation')
        parent.mother_mobile = request.POST.get('mother_mobile')
        parent.mother_email = request.POST.get('mother_email')
        parent.present_address = request.POST.get('present_address')
        parent.permanent_address = request.POST.get('permanent_address')
        parent.save()  # save updated parent data

        
        # update student data
        student.student_id=student_id
        student.first_name=first_name
        student.last_name=last_name
        student.student_class=student_class
        student.section=section
        student.gender = gender
        student.date_of_birth = date_of_birth
        student.religion = religion
        student.admission_number = admission_number
        student.joining_date = joining_date
        student.mobile_number = mobile_number
        student.student_image = student_image        
        student.save()  # save updated student data

        messages.success(request, 'Student updated successfully!')
        return redirect('student_list')
    
    return render(request, 'student/edit-student.html', {'student': student, 'parent': parent})

def delete_student(request, slug):
    if request.method == 'POST':
        student = get_object_or_404(Student, slug=slug)
        student_name = f'{student.first_name} {student.last_name}'
        student.delete()
        messages.success(request, f'{student_name} deleted successfully!')
        return redirect('student_list')

    return HttpResponseForbidden('Cannot delete student')