from django.shortcuts import render
from .models import Job, Application
from payments.models import Balance
# Create your views here.

def joblistings(request):
    jobs = Job.objects.all()
    return render(request, 'joblist.html', {'jobs': jobs})
def jobsapply(request, jobid, User):
    if request.method == 'GET':
        return render(request, 'essaey.html')
    jobdata = Job.objects.get(id=jobid)
    model = Application()
    model.Job = jobdata
    model.User = User.objects.get(Username=User)
    eassy = request.POST['reason']
    if "i want this job" in eassy:
        model.Status = True
        model.save()
        model3 = Balance.objects.get(User=model.User)
        model3.money = model3.money + jobdata.Doctoral_Pay
        model3.save()
        return render(request, 'congrats.html')
    else:
        model.Status = False
        model.save()
        model3 = Balance.objects.get(User=model.User)
        model3.money = model3.money - 1000
        model3.save()
        return render(request, 'failed.html')
    
