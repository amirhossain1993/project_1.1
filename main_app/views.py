from django.shortcuts import render,redirect

# Create your views here.

from .models import *


def index(request):
    user_info = UserInfo.objects.all()
    context = {
        'user_info': user_info
    }
    return render(request, 'index.html',context)

from.forms import Contactform
def contact(request):
    if request.method == 'POST':
        form = Contactform (request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_page')

    else:
        form = Contactform()
        
    return render(request, 'contact.html',{'form':form, 'success':'Form submitted successfully'}) 

def projects(request):
    return render(request, 'projects.html')

def resume(request):
    experience = Experience.objects.all()
    education = Education.objects.all()
    context = {
    
        'experience' : experience,
        'education' : education,
    }
    return render(request, 'resume.html',context)




