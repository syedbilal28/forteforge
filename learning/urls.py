from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path('signup/student/', views.signup, name='signup'),
    path("signup/choice/",views.signup_choice,name='SignupChoice'),
    path('login/', views.login, name='login'),
    path("careers/",views.Careers,name="Careers"),
    path('signup/enterprise/',views.signup_enterprise,name="Signupenterprise"),
    path("events/",views.events,name="Events"),
    path("course/",views.course,name="Course"),
    path("course/instructor/",views.instructor,name="instructor"),
    path("course/overview/",views.overview,name="overview"),
    path("events/live/",views.LiveEvents,name="LiveEvents"),
    path("events/live/1/",views.CurrentLiveEvent,name="CurrentLive"),
    path("courses/industry/specific/",views.IndustrySpecificCourses,name="IndustrySpecific"),
    path("event/details/",views.EventDetails,name="EventDetails"),
    path("enterprise/",views.Enterprise,name="Enterprise")
]
