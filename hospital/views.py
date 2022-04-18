from multiprocessing import context
from django.shortcuts import render,redirect, HttpResponse
import hospital
from hospital.models import Hospital
from tracker.models import Item, Order, Registrations
from .forms import RequestForm
from django.contrib.auth.decorators import login_required
from django.core.serializers import  serialize

# Create your views here.
# @login_required(login_url='/login/')
def hshome(request):
    items = Item.objects.all()
    donor = Registrations.objects.filter(account_type='DONOR')
    loggedin_user = ''
    try:
        loggedin_user = request.COOKIES['loggedin']
        
    except:
        
        return redirect('login')
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
    hospital = Order.objects.all().order_by('-order_date')
    form = RequestForm()
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        item = request.POST.get('item')
        donor = request.POST.get('donor')
        
        if get_user== 'No User':
            error ='User not auntenticated'
        else:
            get_item = Item.objects.get(name=item)
    
            if int(get_item.quantity) > int(quantity):
                new_order = Order(user=current_user,item=item, quantity=quantity, donor_name=donor)
                new_order.save()
                success =" Order placed successfully"
            else:
                error = "Quantity requested exceeds what is in store (" +str( item.quantity) + ")"
            
        
        return redirect('hshome')

    else:
        pass
    args = {
        'hospitals': hospital,
        'form':form,
        'user': loggedin_user,
        'error': error,
        'success': success,
        'items': items,
        'donors':donor,        
    }
  
    return render(request,'hshome.html', args)

def services(request):
  return render(request,'services.html')

def hsrequest(request):
    items = Item.objects.all()
    donor = Registrations.objects.filter(account_type='DONOR')
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
        donor = request.POST.get('donor')
        
        if get_user== 'No User':
            error ='User not auntenticated'
        else:
            get_item = Item.objects.get(name=item)
    
            if int(get_item.quantity) > int(quantity):
                new_order = Order(user=current_user,item=item, quantity=quantity, donor_name=donor)
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
        'donors':donor,
    }
    return render(request, 'hs_request.html', context)

def hospital_dataset(request):
    hospitals = serialize('geojson',Hospital.objects.all())
    return HttpResponse(hospitals, content_type='json')