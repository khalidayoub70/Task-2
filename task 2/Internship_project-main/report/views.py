from django.shortcuts import render,HttpResponse
from django import forms
from django.shortcuts import render
from .models import Intern
from .forms import TaskForm
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.decorators import login_required


def home_page(request):
    # return HttpResponse('<b>Hello Interns<b>')
    return render(request, 'home.html')
# Create your views here.
def submit_work(request):
    interns = Intern.objects.all()
    
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect or display a success message
            return HttpResponseRedirect('/success/')
    else:
        form = TaskForm()
        print('internlist',interns)
    
    return render(request, 'home.html', {'form': form, 'interns': interns})
def Success(request):
    # return HttpResponse('<b>Hello Interns<b>')
    return render(request, 'success.html')

def accounts(request):
    return render(request, 'welcome.html',{'today': datetime.today()})

@login_required
def authorized(request):
    return render(request, 'authorized.html',{})