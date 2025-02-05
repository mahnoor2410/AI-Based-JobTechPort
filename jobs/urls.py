from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('jobs/', views.job_list, name='job_list'),  # Homepage or list of jobs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('job/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('create-job/', views.create_job, name='create_job'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
    path('edit-job/<int:id>/', views.edit_job, name='edit_job'),
    path('delete-job/<int:id>/', views.delete_job, name='delete_job'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update-status/<int:application_id>/', views.update_status, name='update_status'),
    path('update-ai-processing-status/<int:application_id>/', views.update_ai_processing_status, name='update_ai_processing_status'),
]
