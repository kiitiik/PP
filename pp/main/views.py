from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    data = {
        'title':'Главная страница',
        'values': ['some','123','hi'],
        'obj': {
            'car':'kio',
            'age': '22',
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html',data)
def about(request):
    return render(request, 'main/about.html')
@login_required
def video(request):
    return render(request, 'main/video.html')