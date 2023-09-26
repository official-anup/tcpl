from django import forms
#from .models import Customer2
# from .models import UploadedFile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext,gettext_lazy as _ 
from django.contrib.auth import password_validation
from home.models import Customer2

 

class CustomerProfileForms(forms.ModelForm):
    class Meta:
        model=Customer2
        fields=["fullname","mobileno","dob","address","city","pin_code","occupation","industry"] #
        
        widgets={"fullname":forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter Full Name"}),
                 
        "mobileno":forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter Mobile Number"}),

        "dob" :forms.DateInput(attrs={"class":"form-control",'type': 'date'}),

        "address":forms.TextInput(attrs={"class":"form-control","placeholder": "Enter Your address"}),
        
        "city":forms.TextInput(attrs={"class":"form-control","placeholder": "Enter Your address"}),
        
        "pin_code":forms.TextInput(attrs={"class":"form-control","placeholder": "Enter Your address"}),
        
        "occupation":forms.Select(attrs={"class":"form-control","placeholder": "Select Option"}),
        
       
        "industry": forms.Select(attrs={"class": "form-control"}),
        
        }


