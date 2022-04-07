from multiprocessing import context
from django.shortcuts import render,redirect
import hospital
from hospital.models import Hospital
from tracker.models import Item, Order, Registrations
from .forms import RequestForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='/login/')
def hshome(request):
    loggedin_user = ''
    try:
        loggedin_user = request.COOKIES['loggedin']
    except:
        return redirect('login')
    hospital = Order.objects.all()
    title = 'Hospital Page'
    args = {
        'hospitals': hospital,
        'user': loggedin_user,
        'title': title,
        
    }
  
    return render(request,'hshome.html', args)

def services(request):
  return render(request,'services.html')

def hsrequest(request):
    items = Item.objects.all()
    loggedin_user = ''
    try:
        loggedin_user = request.COOKIES['loggedin']
    except:
        return redirect('login')
    error =''
    success = ''
    try:
        get_user = request.COOKIES['loggedin']
        current_user = Registrations.objects.get(email=get_user)
    except:
        get_user= 'No User'

    form = RequestForm()
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        item = request.POST.get('item')
        if get_user== 'No User':
            error ='User not auntenticated'
        else:
            get_item = Item.objects.get(name=item)
    
            if int(get_item.quantity) > int(quantity):
                new_order = Order(user=current_user,item=item, quantity=quantity)
                new_order.save()
                success =" Order placed successfully"
            else:
                error = "Quantity requested exceeds what is in store (" +str( item.quantity) + ")"
            
        
        return redirect('hshome')

    else:
        pass
    context ={
        'error': error,
        'success': success,
        'form': form,
        'user':loggedin_user,
        'items': items,
    }
    return render(request, 'hs_request.html', context)