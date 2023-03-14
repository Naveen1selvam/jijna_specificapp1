from django.shortcuts import render

# Create your views here.
def csk(request):
    d={'name':'MSD','No':7}
    return render(request,'jinja.html',context=d)
