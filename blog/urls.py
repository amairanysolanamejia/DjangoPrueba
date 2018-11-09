from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio,name='inicio'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
