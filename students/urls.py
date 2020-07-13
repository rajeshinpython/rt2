from django.urls import path
from django.views.generic import TemplateView
from students import views
urlpatterns = [
        path('',TemplateView.as_view(template_name='student/frontpage.html'),name='frontpage'),
        path('register/',views.Register.as_view(),name='register'),
        path('slogin/',TemplateView.as_view(template_name='student/login.html'),name='slogin'),
        path('shome/',views.studentHome,name = 'shome'),
]