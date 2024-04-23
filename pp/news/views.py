from django.shortcuts import render
from .models import Artiles
def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request,'news/news_hime.html', {'news': news})