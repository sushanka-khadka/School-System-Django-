from django.contrib import admin

# Register your models here.

from .models import Student, Parent

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    search_fields = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    list_filter = ('father_occupation', 'mother_occupation')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'student_class', 'section', 'gender', 'date_of_birth', 'mobile_number')
    search_fields = ('student_id', 'first_name', 'last_name', 'admission_number', 'student_class')
    list_filter = ('student_class', 'section', 'gender')
    readonly_fields = ('student_image',)    # make student_image read-only in admin interface