from django.shortcuts import render

# Create your views here.
def RCB(request):
    d={'name':'The Wall','No':11}
    return render(request,'jinja.html',context=d)
