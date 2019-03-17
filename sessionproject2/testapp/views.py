from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,'testapp/name.html')

def proces_name_view(request):
    name=request.GET['name']
    response=render(request,'testapp/age.html')
    response.set_cookie('name',name)
    return response

def proces_age_view(request):
    age=request.GET['age']
    response=render(request,'testapp/gf.html')
    response.set_cookie('age',age)
    return response

def results_view(request):
    gfn=request.GET['gfn']
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    return render(request,'testapp/results.html',{'name':name,'age':age,'gfn':gfn})
