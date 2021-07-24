from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path("choice/",views.signup_choice,name='SignupChoice'),
    path('', views.login, name='login'),
    path("home/",views.Home,name="Home"),
]
