from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def donarpage(request):
    title= 'Donor Page'
    context ={
        'title': title,
    }
    return render(request, 'donorindex.html', context)