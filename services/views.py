from django.shortcuts import render

# Create your views here.
def services(request):
    title= 'Our Services'
    context ={
        'title': title,
    }    
    return render(request, 'services.html', context)