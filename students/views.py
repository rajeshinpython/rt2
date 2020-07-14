from django.shortcuts import render,redirect
from django.views.generic import View,ListView
from students.forms import StudentModelForm
from .models import StudentModel
from  Admin1.models import CourseModel
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
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
        StudentModel.objects.get(email=un,password=pas)
        s = StudentModel.objects.get(email=un)
        return render(request,'student/shome.html',{'s':s})

    except ObjectDoesNotExist:
        return render(request, 'student/login.html', {"message": 'Invalid Details'})






class Enroll(ListView):
    model = CourseModel
    template_name = 'student/enroll.html'


def saveEnroll(request,pk):
    spk = request.GET.get('no')
    c = CourseModel.objects.get(pk = pk)
    print(c.name)
    s = StudentModel.objects.get(pk=spk).update(enrol = c.name)
    return render(request,'student/enroll.html',{'message': 'enrolled'})



