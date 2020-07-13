from django import forms
from students.models import StudentModel


class StudentModelForm(forms.Form):
    password = forms.PasswordInput()

    class Meta:
        fields = "__all__"
        model = StudentModel