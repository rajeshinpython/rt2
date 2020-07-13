from django.shortcuts import render
from django.views.generic import View
from students.forms import StudentModelForm
from .models import StudentModel
# Create your views here.
class Register(View):

    def get(self,request):
        s={'rf': StudentModelForm()}
        print(s)
        return render(request,"student/register.html",{'rf': StudentModelForm()})


def frontPage(request):
    return render(request,'student/frontpage.html')