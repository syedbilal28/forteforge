from django.forms import ModelForm
from .models import Student, User


# Create the form class.
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

class ProfileForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'