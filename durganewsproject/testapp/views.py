from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

def movie_news_view(request):
    news1='In Telugu DevDas movie is not Good'
    news2='Salman Updating Minimum 100 Crores Guarantee for his Movies'
    news3='Sonali slowly getting curing'
    news4='Amitabh Bachchan next movie is Thugs of Hindustan'
    news5='Salman and Katrina going to marry soon'
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
    return render(request,'testapp/mnews.html',my_dict)
