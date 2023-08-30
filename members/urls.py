from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('members/', views.members, name='members'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('football/', views.football, name='football'),
    path('general/', views.general, name='general'),
]