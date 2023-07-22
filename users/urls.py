from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.RegisterView, name='register'),
    path('', views.IndexView, name='index'),

]
