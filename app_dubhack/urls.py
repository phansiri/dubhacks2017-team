from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'input_classes_new/', views.input_classes_new, name='input_classes_new'),
    url(r'grabClientData/', views.grabClientData, name='grabClientData'),
]