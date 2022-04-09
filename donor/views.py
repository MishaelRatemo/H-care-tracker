from email.policy import default
from multiprocessing import context
from django.shortcuts import render,redirect

from hospital.models import *
from tracker.models import Order

# Create your views here.
def donarpage(request):
    loggedin_user = ''
    try:
        loggedin_user = request.COOKIES['loggedin']
    except:
        return redirect('login')
    title= 'Donor Page'
    approval_status=Order.objects.filter(status=False)
    requests = Order.objects.all().order_by('order_date')
    context ={
        'title': title,
        'requests': requests,
        'approval':approval_status,
        'user': loggedin_user,
    }
    if request.GET.get('Dispatch') == 'Dispatch':
        req = Order.objects.get(id=id)

        req.delete()
    return render(request, 'donorindex.html', context)