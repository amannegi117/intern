from django.shortcuts import render,redirect
from django.http import request
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method =='POST':
        form = uploadform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            redirect('/')
    form = uploadform()
    img = Image.objects.all()
    return render(request,'myapp/index.html',{'img': img,'form': form})


@login_required
def update(request):
    if request.method=='POST':

        p_form = create_profile(request.POST,request.FILES,instance = request.user.profile)
        if p_form.is_valid():
           
            p_form.save()
            return redirect('profile')
    else:
        u_form = create_user(instance = request.user)
        p_form = create_profile(instance = request.user.profile)
    context={
        'p_form':p_form  }
        

    return render(request,'myapp/update.html',context)

def profile(request):
    return render(request,'myapp/profile.html')






