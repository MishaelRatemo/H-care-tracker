from django.shortcuts import render

# Create your views here.
def contact_us(request):
    title= 'Contact Us'
    context ={
        'title': title,
    }    
    return render(request, 'contact.html', context)