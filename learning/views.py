from django.http.response import JsonResponse
from learning.models import Course, Student
from django.shortcuts import redirect, render, HttpResponse
import json
from learning.serializers import CourseSerializer
# from . import forms
from .forms import EnterpriseContactForm, ProfileForm,UserForm,ContactForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    if request.method =="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index") 
    else:
        form=ContactForm()
        context={"form":form}
        return render(request,"learning/index.html",context)
@csrf_exempt
def login(request):
    if request.method == 'POST':
        return HttpResponse("<h1>Logged In</h1>")
    else:
        form = UserForm()
        return render(request, 'learning/login.html', {'form':form})

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        profileform = ProfileForm(request.POST, request.FILES)
        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            profile = profileform.save(user)
            return HttpResponse("<h1>Signed Up</h1>")
        #for dev
        else:
            raise Exception (f"Profile form not valid {profileform}")
    else:
        userform = UserForm()
        profileform = ProfileForm()
    return render(request, 'learning/signup.html', {'userform':userform, 'profileform':profileform})

def signup_choice(request):
    return render(request,"learning/signup-type.html")

def Careers(request):
    return render(request,"learning/careers.html")

def signup_enterprise(request):
    return render(request,"learning/signup_enterprise.html")

def events(request):
    return render(request,"learning/events.html")

def course(request,course_id):
    course=Course.objects.get(pk=int(course_id))
    context={"course":course}
    return render(request,"learning/course.html",context)

def instructor(request):
    return render(request,"learning/instructor.html")

# def overview(request,course_id):
    
#     return render(request,"learning/overview.html",context)

def LiveEvents(request):
    return render(request,"learning/live-events.html")

def CurrentLiveEvent(request):
    return render(request,"learning/event-live-1.html")

def IndustrySpecificCourses(request):
    return render(request,"learning/industry-specific-courses.html")

def EventDetails(request):
    return render(request,"learning/event-details.html")

def Enterprise(request):
    if request.method =="POST":
        form=EnterpriseContactForm(request.POST)
        if form.is_valid():
            form.save()
            form= EnterpriseContactForm()
            context={"form":form}
            return render(request,"learning/enterprise.html",context)    
    else:
        form= EnterpriseContactForm()
        context={"form":form}
        return render(request,"learning/enterprise.html",context)

def GetCourses(request,keyword):
    courses=Course.objects.filter(category__iexact=keyword)
    courses=CourseSerializer(courses,many=True).data
    return JsonResponse({"courses":courses},status=200)

@csrf_exempt
def AddCourse(request):
    body=json.loads(request.body)
    course_name=body.get("name")
    subcategory=body.get("subcategory")
    category=body.get("category")
    course=Course.objects.create(
        name=course_name,
        subcategory=subcategory,
        category=category
    )
    return HttpResponse(status=201)

def partners(request):
    return render(request,"learning/partners.html")