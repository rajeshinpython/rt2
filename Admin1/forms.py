from django import forms
from Admin1.models import LogInModel

class LogInModelForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput)

    class Meta:
        fields = '__all__'
        model = LogInModel