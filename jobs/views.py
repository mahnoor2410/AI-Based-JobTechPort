from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.core.exceptions import ValidationError
from .models import Job, Application
from .forms import ResumeUploadForm, JobForm, CustomUserCreationForm, JobCreationForm
from .ai import extract_text_from_pdf, rank_resume
from django.core.mail import send_mail
from django.conf import settings
import os

# ========================================= Home Page ==================================

def home_view(request):
    return render(request, 'jobs/home.html')

# ========================================= Register View ==================================

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Welcome {user.username}!")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'jobs/register.html', {'form': form})

# ========================================= Login View ==================================

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) # built in form for authentication(username, pass)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('job_list')
    else:
        form = AuthenticationForm()
    return render(request, 'jobs/login.html', {'form': form})

# ========================================= Logout View ==================================

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('job_list')

# =========================================  All Jobs List View ==================================

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

# ========================================= Apply Job View ==================================

def apply_job(request, job_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    job = get_object_or_404(Job, id=job_id)
    
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user # current logged-in user ko represent karta hai.
            application.job = job # current job represent karta hai jis me user abi he
            application.status = 'Pending' # by default user see pending status until admin accept or reject
            
            resume_file = application.resume # "resume" came from model
            if not resume_file:
                raise ValidationError("No file uploaded.")
            
            application.save()
            
            # AI Processing for resume that uploaded above by user
            if resume_file.name.endswith('.pdf'):
                resume_path = resume_file.path # path get
                if os.path.exists(resume_path):
                    resume_text = extract_text_from_pdf(resume_path) # it goes to ai.py 
                    job_description = job.description # it also goes to ai.py for processing
                    rank_score = rank_resume(resume_text, job_description)
                    
                    application.ai_rank_score = rank_score  # Store AI score but don't change status
                    application.save()
            
            return redirect('user_dashboard')
    else:
        form = ResumeUploadForm()
    
    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})

# ========================================= User Dashboard View ==================================

def user_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    applications = Application.objects.filter(user=request.user)
    return render(request, 'jobs/user_dashboard.html', {'applications': applications})

# ========================================= Admin Dashboard View ==================================

@staff_member_required
def admin_dashboard(request):
    applications = Application.objects.all()
    return render(request, 'jobs/admin_dashboard.html', {'applications': applications})

# ========================================= Update Application Status ==================================

@staff_member_required
def update_status(request, application_id):
    if request.method == 'POST':
        # update status rejected/accepted
        application = get_object_or_404(Application, id=application_id) # appliaction ko id se get kr rhy
        new_status = request.POST.get('status') #  Get this "status" from "form"(admin template waly form se)
        
        if new_status not in ['Accepted', 'Rejected', 'Pending']:
            return HttpResponseForbidden("Invalid status.")
        
        application.status = new_status # admin jo click kry ga is me aa k save hoga  
        application.save()

        # Email Notification
        subject = ""
        message = ""
        
        if new_status == "Accepted":
            subject = "Congratulations! You are selected for an interview"
            message = f"Dear {application.user.username},\n\n"
            message += "We are pleased to inform you that you have been selected for an interview. "
            message += "Please respond to schedule your interview (Online/Onsite).\n\n"
            message += "Best regards,\nYour Hiring Team - JobTechPort"

        elif new_status == "Rejected":
            subject = "Application Status Update"
            message = f"Dear {application.user.username},\n\n"
            message += "We appreciate your interest in the position. Unfortunately, we have decided to move forward with other candidates at this time.\n\n"
            message += "Best wishes for your future opportunities.\nYour Hiring Team - JobTechPort"

        # Send email if status is updated to Accepted or Rejected
        if new_status in ["Accepted", "Rejected"]:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,  # From email address
                [application.user.email], # User's email address
                fail_silently=False, # if error occur
            )

        return redirect('admin_dashboard')

    return HttpResponseForbidden("Invalid request method.")

# ========================================= Update AI Processing Status ==================================

@staff_member_required
def update_ai_processing_status(request, application_id):
    if request.method == 'POST':
        application = get_object_or_404(Application, id=application_id)
        new_processing_status = request.POST.get('ai_processing_status')
        
        if new_processing_status not in ['Pending', 'Processed']:
            return HttpResponseForbidden("Invalid AI processing status.")
        
        application.ai_processing_status = new_processing_status
        application.save()
        return redirect('admin_dashboard')
    
    return HttpResponseForbidden("Invalid request method.")

# ========================================= Create Job View ==================================

@login_required
def create_job(request):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to create jobs.")
        return redirect('job_list')
    
    if request.method == 'POST':
        form = JobCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Job created successfully!")
            return redirect('job_list')
    else:
        form = JobCreationForm()
    
    return render(request, 'jobs/create_job.html', {'form': form})

# ========================================= Job Detail View ==================================

def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    
    return render(request, 'jobs/job_detail.html', {'job': job})

# ========================================= Edit Job View ==================================

def edit_job(request, id):
    if not request.user.is_staff:
        return redirect('job_list')
    
    job = get_object_or_404(Job, id=id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job)
    
    return render(request, 'jobs/edit_job.html', {'form': form, 'job': job})

# ========================================= Delete Job View ==================================

def delete_job(request, id):
    if not request.user.is_staff:
        return redirect('job_list')
    
    job = get_object_or_404(Job, id=id)
    job.delete()
    return redirect('job_list')


