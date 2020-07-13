"""rt2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from Admin1 import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home,name='main'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('check_adlogin/', views.check_Adlogin, name='check_login'),
    path('addclass/', views.AddClass.as_view(), name='addclass'),
    path('viewclass/', views.ViewCourse.as_view(), name='viewclass'),
    path('update/<int:pk>/', views.UpdateViews.as_view(), name='updatecourse'),
    path('deletecourse/<int:pk>', views.deletecourse, name='deletecourse'),
    path('home/', TemplateView.as_view(template_name='Admin/adhome.html'), name='home'),


    path('students/',include('students.urls')),

]

