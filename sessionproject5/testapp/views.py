from django.shortcuts import render
from testapp.forms import AddItemForm

# Create your views here.
def add_item_view(request):
    form=AddItemForm()
    submit=False
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['qunatity']
        request.session[name]=quantity
        request.session.set_expiry(180)
        submit=True
    return render(request,'testapp/additem.html',{'form':form,'submit':submit})

def display_items_view(request):
    return render(request,'testapp/displayitems.html')
