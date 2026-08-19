from django.contrib import admin
from .models import Department, ProjectType, InterviewType, Job, Stage, Applicant, Interview, Offer

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ProjectType)
class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(InterviewType)
class InterviewTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'direct_manager', 'start_date')
    list_filter = ('department', 'project_type')

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('job', 'title', 'order')

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job', 'current_stage', 'email')
    list_filter = ('job', 'current_stage')

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'interview_type', 'date_time', 'result')

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'offer_date', 'amount', 'result')
