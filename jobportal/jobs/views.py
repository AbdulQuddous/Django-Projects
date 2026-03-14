from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import Profile,Job,Application
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
def register(request):

    form = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            Profile.objects.create(
                user=user,
                role=form.cleaned_data['role']
            )

            return redirect("login")

    return render(request,'register.html',{'form':form})


class JobListView(ListView):
    model = Job
    template_name = 'job_list.html'
    context_object_name = 'jobs'
    paginate_by = 5   # adjust as needed

class JobDetailView(DetailView):
    model = Job
    template_name = "job_detail.html"
    context_object_name = 'job'

class JobCreateView(CreateView):
    model = Job
    fields = ['title','description','company_name','salary','location']
    success_url = "/"
    def form_valid(self,form):

        form.instance.posted_by = self.request.user

        return super().form_valid(form)

class JobUpdateView(UpdateView):   
    model = Job
    fields = ['title','description','company_name','salary','location']
    template_name = "job_form.html"
    success_url = "/"


class JobDeleteView(DeleteView):  
    model = Job
    template_name = "job_confirm_delete.html"
    success_url = "/"


    

@login_required
def apply_job(request,job_id):

    job = Job.objects.get(id=job_id)

    if Application.objects.filter(job=job,applicant=request.user).exists():

        messages.error(request,"Already applied")

        return redirect("job_detail",pk=job.id)

    if request.method == "POST":

        resume = request.FILES['resume']

        Application.objects.create(
            job=job,
            applicant=request.user,
            resume=resume
        )

        messages.success(request,"Application submitted")

    return redirect("job_detail",pk=job.id)

def save_jobs(request,job_id):

    saved = request.session.get('saved_jobs',[])

    if job_id not in saved:
        saved.append(job_id)

    request.session['saved_jobs'] = saved

    return redirect("job_list")

def set_theme(request):

    theme = request.GET.get("theme")

    response = redirect("/")

    response.set_cookie("theme",theme)

    return response

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Job, Application


@login_required
def recruiter_dashboard(request):

    # jobs posted by recruiter
    jobs = Job.objects.filter(posted_by=request.user)

    # applications for recruiter jobs
    applications = Application.objects.filter(job__posted_by=request.user)

    context = {
        'jobs': jobs,
        'applications': applications
    }

    return render(request, 'recruiter_dashboard.html', context)

def job_search(request):

    query = request.GET.get('q')

    jobs = Job.objects.filter(

        Q(title__icontains=query) |
        Q(company_name__icontains=query) |
        Q(location__icontains=query)

    )

    return render(request,"job_list.html",{'jobs':jobs})