from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,ListView,UpdateView,DeleteView
from Admin1.forms import LogInModelForm
from Admin1.models import LogInModel,CourseModel
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
class LogIn(View):

    def get(self,request):
        context = {"lf": LogInModelForm()}
        return render(request,"Admin/adlogin.html",context)

    #def post(self,request):
        # al = LogInForm(request.POST)
        # print(al)
        # if al.is_valid():
        # un = request.POST.get("username")
        # print(un)
        # pas = request.POST.get("password")
        # try:
        #     LogIn(username=un,password=pas)
        #     return HttpResponse(request,"Admin/adhome.html")
        # except ValueError:
        #     return HttpResponse(request,"Admin/adlogin.html")

        # else:
        #
        #     return redirect('login')


def check_Adlogin(request):
    un = request.POST.get("username")
    pas = request.POST.get("password")
    try:
        LogInModel.objects.get(username=un,password=pas)
        return render(request,"Admin/adhome.html")
    except LogInModel.DoesNotExist:
        context = {"lf": LogInModelForm(),"message":"Invalid Details"}
        return render(request,"Admin/adlogin.html",context)


class AddClass(CreateView):
    template_name = 'Admin/addclass.html'
    fields = '__all__'
    model = CourseModel
    success_url = '/addclass/'


class ViewCourse(ListView):
    template_name = 'Admin/viewclass.html'
    model = CourseModel


class UpdateViews(UpdateView):
    template_name = "Admin/cupdate.html"
    model = CourseModel
    fields = '__all__'
    success_url = '/viewclass/'


# class Deletecourse(DeleteView):
#     template_name = "Admin/delete.html"
#     model = CourseModel
#     success_url = '/viewclass/'


def deletecourse(request,pk):
    CourseModel.objects.get(id=pk).delete()
    return redirect('viewclass')