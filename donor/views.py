from email.policy import default
from multiprocessing import context
from tabnanny import check
from django.shortcuts import render,redirect

from hospital.models import *
from tracker.models import Order
from hospital.models import order_status
from django.core.paginator import  Paginator

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
    
    paginator = Paginator(requests, 5)
    page_num = request.GET.get('page')
    
    page = paginator.get_page(page_num)
    
    paginater = Paginator(requests, 4)
    page_number = request.GET.get('page')
    
    pg = paginater.get_page(page_number)
    
    
    context ={
        'title': title,
        'page': page,
        'pg':pg,  
        'requests':requests,    
        
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
    