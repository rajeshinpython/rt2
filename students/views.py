from django.shortcuts import render,redirect
from django.views.generic import View
from students.forms import StudentModelForm
from .models import StudentModel
from django.contrib import messages
# Create your views here.
class Register(View):

    def get(self,request):
        s={'rf': StudentModelForm()}
        return render(request,"student/register.html",{'rf': StudentModelForm()})

    def post(self,request):
        res = StudentModelForm(request.POST)
        if res.is_valid():
            res.save()
            return render(request,"student/register.html",{'message':'Registeration Sucessful','rf': StudentModelForm()})
        else:
            return render(request,"student/register.html",{'message': res.errors,'rf':StudentModelForm()})


def studentHome(request):
    un = request.POST.get('un')
    pas =request.POST.get('pas')
    try:
        StudentModel(email=un,password=pas)
        s = StudentModel.objects.get(email=un)
        return render(request,'student/shome.html',{'s':s})
    except ValueError:
        messages.error(request,"Invalid Details..!")
        redirect('login')