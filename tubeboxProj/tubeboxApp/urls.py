from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login),
    path('register/', views.register),
    path('youtube/', views.youtube),
    path('process/', views.process_data, name='process_data'),
    path('searchVideo/', views.search_video, name='search_video'),
    
]
