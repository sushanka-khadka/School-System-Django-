from django.db import models

# Create your models here.

class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=100)
    father_email = models.EmailField(max_length=100)
    
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    mother_mobile = models.CharField(max_length=100)
    mother_email = models.EmailField(max_length=100)
    present_address = models.CharField(max_length=100)
    permanent_address =models.CharField(max_length=100)

    def __str__(self):
        return f'{self.father_name} & {self.mother_name}'
    
class Student(models.Model):
    student_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=15)
    section = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')])
    date_of_birth = models.DateField()
    religion = models.CharField(max_length=100)
    admission_number =models.CharField(max_length=15)
    joining_date =models.DateField()
    mobile_number = models.CharField(max_length=10)    
    student_image = models.ImageField(upload_to='student_images/', blank=True, null=True)

    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)     # one-to-one relationship with Parent model
    slug = models.CharField(max_length=100, unique=True, blank=True)    # auto-generated field

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.student_id})'
    
    # Auto-generate slug field before saving
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{self.first_name.lower()}-{self.last_name.lower()}-{self.student_id}'

        return super().save(*args, **kwargs)        # call the original save methodod