from learning.models import Student
from django.shortcuts import redirect, render, HttpResponse
# from . import forms
from .forms import ProfileForm,UserForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request,"learning/index.html")
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

def Home(request):
    return render(request,"learning/home.html")

def signup_enterprise(request):
    return render(request,"learning/signup_enterprise.html")