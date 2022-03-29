from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def home(request):
    title= ' Welcome'
    context ={ 'title': title}
    return render(request, 'index.html', context)