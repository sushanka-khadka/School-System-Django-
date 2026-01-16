from django.shortcuts import render,redirect
from django.contrib import messages

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
        slug = request.POST.get('slug')

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
            slug = slug
        )

        messages.success(request, 'Student added successfully!')
        return redirect('student-list')
    
    return render(request, 'student/add-student.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student-list.html', {'students': students})