from django.shortcuts import render
from testapp.forms import *

# Create your views here.
def name_view(request):
    form=NameForm()
    return render(request,'testapp/name.html',{'form':form})

def process_name_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=AgeForm()
    return render(request,'testapp/age.html',{'form':form})

def process_age_view(request):
    age=request.GET['age']
    request.session['age']=age
    form=GFNameForm()
    return render(request,'testapp/gf.html',{'form':form})

def process_gfname_view(request):
    gfname=request.GET['gfname']
    request.session['girl friend name']=gfname
    # name=request.session['name']
    # age=request.session['age']
    return render(request,'testapp/results.html')
