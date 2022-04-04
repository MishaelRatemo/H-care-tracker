from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def about_us(request):
    title= 'About Us'
    context ={
        'title': title,
    }    
    return render(request, 'about_us.html', context)