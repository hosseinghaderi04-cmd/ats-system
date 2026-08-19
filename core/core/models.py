from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProjectType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class InterviewType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    direct_manager = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    responsibilities = models.TextField()
    requirements = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Stage(models.Model):
    job = models.ForeignKey(Job, related_name='stages', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.job.title} - {self.title}"

class Applicant(models.Model):
    job = models.ForeignKey(Job, related_name='applicants', on_delete=models.CASCADE)
    current_stage = models.ForeignKey(Stage, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    key_info = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Interview(models.Model):
    applicant = models.ForeignKey(Applicant, related_name='interviews', on_delete=models.CASCADE)
    interviewers = models.ManyToManyField(User)
    interview_type = models.ForeignKey(InterviewType, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    result = models.CharField(max_length=100, blank=True)
    evaluation = models.TextField(blank=True)

    def __str__(self):
        return f"{self.applicant.full_name} - {self.interview_type.name}"

class Offer(models.Model):
    applicant = models.ForeignKey(Applicant, related_name='offers', on_delete=models.CASCADE)
    offer_date = models.DateField()
    amount = models.CharField(max_length=100)
    result = models.CharField(max_length=100, blank=True)
    reject_reason = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.applicant.full_name} - Offer"
