from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def about_us(request):
    loggedin_user =''
    try:
        loggedin_user = request.COOKIES['loggedin']
    except:
        pass
    title= 'About Us'
    context ={
        'title': title,
        'user':loggedin_user
    }    
    return render(request, 'about_us.html', context)