from django.db import models

# ====================================== Job model =========================================

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ====================================== for admin side =========================================

class Application(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)  # Jo user apply kar raha hai
    job = models.ForeignKey(Job, on_delete=models.CASCADE) # Jo job ke liye apply kar raha hai
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending')
    ai_rank_score = models.IntegerField(null=True, blank=True)  # Field to store the AI ranking score
    ai_processing_status = models.CharField(max_length=20, choices=[('Processing', 'Processing'), ('Completed', 'Completed')], default='Processing')
    created_at = models.DateTimeField(auto_now_add=True) # Application ka creation time.

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"


