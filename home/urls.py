from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('about/', views.about_us, name='about')
]

# 1:54 parte 1