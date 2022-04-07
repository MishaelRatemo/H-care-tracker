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

    hospital = Order.objects.all()
    orders_approved = Order.objects.filter(status=True)
    args = {
        'hospitals': hospital,
        'orders':orders_approved
    }
  
    return render(request,'hshome.html', args)

def services(request):
  return render(request,'services.html')

def hsrequest(request):
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
            get_item = Item.objects.filter(name=item)
            if get_item.exists():
                for item in get_item:
                    # print('###################')
                    # print(item.quantity)
                    if int(item.quantity) > int(quantity):
                        new_order = Order(user=current_user,item=item, quantity=quantity)
                        new_order.save()
                        success =" Order placed successfully"
                    else:
                        error = "Quantity requested exceeds what is in store (" +str( item.quantity) + ")"
            else:
                error ="Item not available"
        
        return redirect('hshome')

    else:
        pass
    context ={
        'error': error,
        'success': success,
        'form': form,
    }
    return render(request, 'hs_request.html', context)