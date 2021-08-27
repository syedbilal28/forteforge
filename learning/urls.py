from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path('signup/', views.signup, name='signup'),
    path("choice/",views.signup_choice,name='SignupChoice'),
    path('login/', views.login, name='login'),
    path("careers/",views.Careers,name="Careers"),
    path('signup/enterprise/',views.signup_enterprise,name="Signupenterprise"),
    path("events/",views.events,name="Events")
]
