from django.shortcuts import render
from .models import Job, Application

# Create your views here.

def joblistings(request):
    jobs = Job.objects.all()
    return render(request, 'joblist.html', {'jobs': jobs})
def jobapply(request, jobid):
    jobdata = job.objects.get(id=jobid)
    model = Application()
    model.Job = jobdata
    model.User = request.User
    eassy = request.POST['reason']
    if "i want this job" in eassy:
        model.Status = True
        model.save()
        return render(request, 'congrats.html')
    else:
        model.Status = False
        return render(request, 'failed.html')
