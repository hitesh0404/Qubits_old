from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    n= 'Nilesh'
    # return HttpResponse(f'hello {name}')
    context = {
        'name': n
    }
    return render(request,'index.html',context)