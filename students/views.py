from django.shortcuts import render,redirect
from django.views.generic import View,ListView
from students.forms import StudentModelForm
from .models import StudentModel
from  Admin1.models import CourseModel
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from students.utils import setexpiry
from django.contrib.sessions.backends.base import SessionBase





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
        request.session['STATUS']=True
        request.session['student_contact'] = s.contact
        return render(request,'student/shome.html',{'s':s})

    except ObjectDoesNotExist:
        return render(request, 'student/login.html', {"message": 'Invalid Details'})





class Enroll(ListView):
    model = CourseModel
    template_name = 'student/enroll.html'


def saveEnroll(request,pk):
    setexpiry(request,100000)
    spk = request.session['student_contact']
    print(spk)
    c = CourseModel.objects.get(pk = pk)
    print(c.name)
    s = StudentModel.objects.get(pk=spk)
    s.enrol.add(c)
    print(s.name)
    messages.success(request,"Enrolled Successfully")
    return redirect("enroll")



def viewenroll(request):
    spk = request.session['student_contact']
    s=StudentModel.objects.get(pk=spk)
    c = s.enrol.all()
    p =[]
    for i in c:
        q = CourseModel.objects.filter(id=i.id).all().values()
        p.append(q)
    return render(request,'student/saveenrol.html',{'course': p })


# class Enroll(ListView):
#     model = CourseModel
# #     template_name = 'student/enroll.html'
def cancelenroll(request):
    spk = request.session['student_contact']
    s = StudentModel.objects.get(pk=spk)
    c = s.enrol.all()
    p = []
    for i in c:
        q = CourseModel.objects.filter(id=i.id).all().values()
        p.append(q)
    return render(request, 'student/cancelenrl.html', {'course': p})


def enroll(request,pk):
    spk = request.session['student_contact']
    s = StudentModel.objects.get(pk=spk)
    s.enrol.remove(pk)
    return redirect('cancel_enroll')
