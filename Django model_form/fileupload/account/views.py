from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import profileform
from .models import Profile
# Create your views here.

def upload(request):
    if request.method=="POST":
        form = profileform(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request  , 'Image upladed Successfully')
            return redirect("profile_view")
        else:
            messages.error(request, 'Error in uplading image')
    else:
        form = profileform()

    return render(request , 'account/upload.html', {'form':form})

def profile_view(request):
    profiles = Profile.objects.all()
    return render(request , 'account/profile_view.html',{'profiles':profiles})