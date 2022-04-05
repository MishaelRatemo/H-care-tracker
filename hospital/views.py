from django.shortcuts import render,redirect
from .forms import RequestForm

# Create your views here.

def hshome(request):


  return render(request,'hshome.html')

def services(request):
  return render(request,'services.html')

def hsrequest(request):
    current_user = request.user
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