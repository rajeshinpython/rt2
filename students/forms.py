from django import forms
from students.models import StudentModel


class StudentModelForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Name"}))
    contact = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':"Contact No"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': "Email ID"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))

    class Meta:
        fields = ["name","contact",'email','password']
        model = StudentModel


    def clean_contact(self):
        cno = str(self.cleaned_data['contact'])
        if len(cno) != 10:
            raise forms.ValidationError("Invalid Contact Number")
        return cno