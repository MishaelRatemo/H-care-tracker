from django.shortcuts import render,redirect

import hospital
from hospital.models import Hospital
from .forms import RequestForm

# Create your views here.

def hshome(request):

    hospital = Hospital.objects.all()
    args = {
        'hospitals': hospital
    }
  
    return render(request,'hshome.html', args)

def services(request):
  return render(request,'services.html')

def hsrequest(request):
    current_user = request.user
    hospital = Hospital.objects.all()
    
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.save()
        return redirect('hshome')

    else:
        form = RequestForm()
    return render(request, 'hs_request.html', {"form": form})