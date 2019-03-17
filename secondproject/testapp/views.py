from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def date_time_view(request):
    date=datetime.datetime.now()
    s='<h1>The Current Date and Time at Server is :' + str(date)+'</h1>'
    return HttpResponse(s)
