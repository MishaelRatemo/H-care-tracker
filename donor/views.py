from multiprocessing import context
from django.shortcuts import render

from hospital.models import *
from tracker.models import Order

# Create your views here.
def donarpage(request):
    title= 'Donor Page'
    
    requests = Order.objects.all().order_by('order_date')
    context ={
        'title': title,
        'requests': requests,
    }
    if request.GET.get('Dispatch') == 'Dispatch':
        req = Order.objects.get(id=id)

        req.delete()
    return render(request, 'donorindex.html', context)