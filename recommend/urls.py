from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('songview/', views.songview, name='songview'),
    path('home/<name>/', views.home, name='home'),
]
