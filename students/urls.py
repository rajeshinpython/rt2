from django.urls import path
from django.views.generic import TemplateView
from students import views
urlpatterns = [
        path('student/',TemplateView.as_view(template_name='student/frontpage.html'),name='frontpage'),
        path('register/',views.Register.as_view(),name='register')
]