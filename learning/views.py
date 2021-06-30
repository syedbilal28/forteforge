from learning.models import Student
from django.shortcuts import redirect, render, HttpResponse
from . import forms
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = request.POST
        return HttpResponse("<h1>Logged In</h1>")
    else:
        form = forms.UserForm()
        return render(request, 'learning/login.html', {'form':form})

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = request.POST
        return HttpResponse("<h1>Signed Up</h1>")
    else:
        userform = forms.UserForm()
        profileform = forms.ProfileForm()
        return render(request, 'learning/signup.html', {'userform':userform, 'profileform':profileform})