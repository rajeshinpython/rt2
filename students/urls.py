from django.urls import path
from django.views.generic import TemplateView
from students import views





urlpatterns = [
        path('',TemplateView.as_view(template_name='student/frontpage.html'),name='frontpage'),
        path('register/',views.Register.as_view(),name='register'),
        path('slogin/',TemplateView.as_view(template_name='student/login.html'),name='slogin'),
        path('shome/',views.studentHome,name = 'shome'),
        path('enroll/',views.Enroll.as_view(),name = 'enroll'),
        path('save_enroll/<int:pk>/',views.saveEnroll,name='save_enroll'),
        path('view_enroll/',views.viewenroll, name = 'viewenroll'),
        path('cancel_enroll/',views.cancelenroll, name = 'cancel_enroll'),
        path('unenroll/<int:pk>/',views.enroll,name = 'unenroll')
]