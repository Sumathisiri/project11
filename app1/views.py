from django.shortcuts import render

# Create your views here.

def project11(request):
    d={'name':'suresh','Age':28,'graduation':'mechanical'}
    return render(request,'jinja_print.html',context=d)


def first(request):
    d={'name':'peddakka'}
    return render(request,'jinja_print.html',context=d)


