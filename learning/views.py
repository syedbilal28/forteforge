from learning.models import Student
from django.shortcuts import redirect, render, HttpResponse
from . import forms
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World</h1>")

@csrf_exempt
def signup(request):
    if request.method == "POST":
        # student_data = Student.objects.create(first_name=request.POST.get())
        return HttpResponse("<h1>Submitted</h1>")
    else:
        userform = forms.UserSignUpForm()
        profileform = forms.ProfileSignUpForm()
        return render(request, 'learning/signup.html', {'userform':userform, 'profileform':profileform})