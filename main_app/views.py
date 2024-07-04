from django.shortcuts import render

# Create your views here.

from .models import UserInfo


def index(request):
    user_info=UserInfo.objects.all()
    context = {
        'user_info': user_info
    }
    return render(request, 'index.html',context)

def contact(request):
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html')

def resume(request):
    return render(request, 'resume.html')




