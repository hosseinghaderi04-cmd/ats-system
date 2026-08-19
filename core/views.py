from django.shortcuts import render
from django.http import JsonResponse
from .models import Job, Stage, Applicant

def home(request):
    return render(request, 'home.html')

def get_job_stages(request, job_id):
    stages = Stage.objects.filter(job_id=job_id).order_by('order')
    data = []
    for stage in stages:
        data.append({
            'id': stage.id,
            'title': stage.title,
            'applicants': list(stage.applicant_set.values('id', 'full_name', 'email'))
        })
    return JsonResponse(data, safe=False)
