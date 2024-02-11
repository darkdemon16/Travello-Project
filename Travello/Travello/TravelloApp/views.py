from django.shortcuts import render,redirect
from . models import Nspot,Ispot
from django.contrib.auth.forms import UserCreationForm
from.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import PassengerDetailForm

# Create your views here.
def index(req):
    nspots = Nspot.objects.all()
    context={}
    context["nspots"]=nspots
    return render(req,'index.html',context)

def international(req):
    ispots = Ispot.objects.all()
    context={}
    context["ispots"]=ispots
    return render(req,'international.html',context)

def register(req):
    form =CreateUserForm()
    if req.method=='POST':
        #form=UserCreationForm(req.POST)
        form =CreateUserForm(req.POST)
        if form.is_valid():
            form.save()
            print('User Created Successfully')
            messages.success(req,("User Created Successfully"))
            return redirect('login/')
        else:
            print('Error')
            messages.error(req,("incorrect username or password Formate"))
    context={'form':form}
    return render(req,"register.html",context)

def login_user(req):
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        user=authenticate(req,username=username,password=password)
        if user is not None:
            login(req,user)
            print("User Logged In Successfully")
            messages.success(req,("User Logged In Successfully"))
            return redirect("/")
        else:
            messages.error(req,("there was an error .Try again "))
            return redirect("/login_user")
    else:
        return render(req,"login.html")
    
def logout_user(req):
    logout(req)
    messages.success(req,("Logged Out Suucesfully"))
    return redirect('/')

def spotdetails(req,pid):
    nspots = Nspot.objects.get(nspot_id=pid)
    context={}
    context['nspots']=nspots
    return render(req,'spotdetails.html',context)

def spotdetails1(req,pid):
    ispots = Ispot.objects.get(ispot_id=pid)
    context={}
    context['ispots']=ispots
    return render(req,'spotdetails1.html',context)

def passenger_detail(request):
    if request.method == 'POST':
        form = PassengerDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a success page
    else:
        form = PassengerDetailForm()
    return render(request, 'passenger_detail.html', {'form': form})
