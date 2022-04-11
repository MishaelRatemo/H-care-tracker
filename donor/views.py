from multiprocessing import context
from tabnanny import check
from django.shortcuts import render,redirect

from hospital.models import *
from tracker.models import Order
from hospital.models import order_status

# Create your views here.
def donarpage(request):
    loggedin_user = ''
    try:
        loggedin_user = request.COOKIES['loggedin']
    except:
        return redirect('login')
    title= 'Donor Page'
    status = order_status.objects.all()
    
    requests = Order.objects.all().order_by('-order_date')
    context ={
        'title': title,
        'requests': requests,
        'user': loggedin_user,
        'status':status,
    }
    # if request.GET.get('Dispatch') == 'Dispatch':
    #     req = Order.objects.get(id=id)

    #     req.delete()
    return render(request, 'donorindex.html', context)
def makepending(request,id):
    item =Order.objects.get(id=id)
    item.status = 'Dispatched'
    item.save()
    return redirect('donorhomepg')

def rejectreq(request,id):
    item =Order.objects.get(id=id)
    item.status = 'Rejected'
    item.save()
    return redirect('donorhomepg')
    