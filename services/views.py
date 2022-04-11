from django.shortcuts import render

# Create your views here.
def services(request):
    loggedin_user =''
    try:
        loggedin_user = request.COOKIES['loggedin']
    except:
        pass
    title= 'Our Services'
    context ={
        'title': title,
        'user': loggedin_user,
    }    
    return render(request, 'services.html', context)