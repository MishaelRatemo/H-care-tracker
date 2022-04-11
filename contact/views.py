from django.shortcuts import render

# Create your views here.
def contact_us(request):
    loggedin_user =''
    try:
        loggedin_user = request.COOKIES['loggedin']
    except:
        pass
    title= 'Contact Us'
    context ={
        'title': title,
        'user': loggedin_user
    }    
    return render(request, 'contact_us.html', context)
