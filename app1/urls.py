from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.index, name = 'index-list'),
    path('post/', views.post , name = 'post-list'),
    path('contact/', views.contact, name = 'contact-list'),
    path('about/', views.contact, name = 'about-list'),
]