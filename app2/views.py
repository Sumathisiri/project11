from django.shortcuts import render

# Create your views here.

def project(request):
    d={'name':'srujana','Age':25}
    return render(request,'jinja_print.html',context=d)

def second(request):
    d={'name':'sudhakar'}
    return render(request,'jinja_print.html',context=d)