from django.forms import ModelForm
from .models import Student, User,Contact


# Create the form class.
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
    
    def save(self, commit=False):
        user = User.objects.create(
            username = self.cleaned_data["email"].split('@')[0],
            first_name = self.cleaned_data["first_name"],
            last_name = self.cleaned_data["last_name"],
            email = self.cleaned_data["email"],
            password = self.cleaned_data["email"],
        )

        return user

class ProfileForm(ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['dob', 'postal_code', 'street_name', 'city', 'state', 'country', 'portfolio']
    def save(self, user, commit=False):
        student = Student.objects.create(
            user = user,
            dob = self.cleaned_data["dob"],
            postal_code = self.cleaned_data["postal_code"],
            street_name = self.cleaned_data["street_name"],
            city = self.cleaned_data["city"],
            state = self.cleaned_data["state"],
            country = self.cleaned_data["country"],
            portfolio = self.cleaned_data["portfolio"]
        )
        return student

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['city'].empty_label = "City"
        self.fields['country'].empty_label = "Country"
