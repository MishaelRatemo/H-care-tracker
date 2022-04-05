from multiprocessing import context
from django.shortcuts import render

from hospital.models import *

# Create your views here.
def donarpage(request):
    title= 'Donor Page'
    
    requests = Hospital.objects.all().order_by('date_created')
    context ={
        'title': title,
        'requests': requests,
    }
    return render(request, 'donorindex.html', context)