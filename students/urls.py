from django.urls import path
from django.views.generic import TemplateView
from students import views
urlpatterns = [
        path('',views.frontPage,name='frontpage'),
        path('register/',views.Register.as_view(),name='register')
]