from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser  # Import custom user model
from .models import Application, Job

# =============================
# Resume Upload Form
# =============================
class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume']

# =============================
# Custom User Registration Form
# =============================
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email' , 'first_name' , 'last_name')  

# =============================
# Job Creation Form
# =============================
class JobCreationForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'company', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

# =============================
# Job Update Form
# =============================
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'company', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }
