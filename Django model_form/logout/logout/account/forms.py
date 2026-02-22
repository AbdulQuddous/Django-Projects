from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    
class Registration_form(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
       model = User
       fields = ['username','email','password1','password2']

    def clean_email(self):
        data = self.cleaned_data.get("email")
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email address is already registered.")
        return data
    
    

       
