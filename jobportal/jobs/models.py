from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):

    ROLE_CHOICES = (
        ('recruiter','Recruiter'),
        ('seeker','Job Seeker')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES)
    profile_image = models.ImageField(upload_to="profiles/",null=True,blank=True)

    def __str__(self):
        return self.user.username
    
class Job(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    company_name = models.CharField(max_length=200)
    salary = models.IntegerField()
    location = models.CharField(max_length=200)

    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Application(models.Model):

    STATUS_CHOICES = (
        ('pending','Pending'),
        ('shortlisted','Shortlisted'),
        ('rejected','Rejected')
    )

    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    applicant = models.ForeignKey(User,on_delete=models.CASCADE)

    resume = models.FileField(upload_to="resumes/")

    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant} - {self.job}"