from django.shortcuts import render

# Create your views here.
def page_count_view(request):
    count=request.session.get('count',0)
    newcount=count+1
    request.session['count']=newcount
    request.session.set_expiry(180)
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request,'testapp/count.html',{'count':newcount})
