from django import forms
from home_auth.models import CustomUser

class UserRoleForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'is_admin', 'is_student', 'is_teacher', 'is_active']
        widgets = {
            'is_admin': forms.CheckboxInput(),
            'is_student': forms.CheckboxInput(),
            'is_teacher': forms.CheckboxInput(),
            'is_active': forms.CheckboxInput(),
        }