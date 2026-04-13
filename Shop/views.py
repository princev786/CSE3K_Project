from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import Contact
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    return render(request,'index.html')
def products(request):
    return render(request,'products.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        emailid=request.POST.get('email')
        msg=request.POST.get('msg')
        c = Contact(name=name,phone=phone,emailid=emailid,msg=msg)
        c.save()
        return redirect('/contact')
    data = Contact.objects.all() #list of all objects
    return render(request,'contact.html',{"data":data})

def catalogue(request):
    return render(request,'catalogue.html')

def loginView(request):
    if request.method=="POST":
        userName = request.POST.get('userName')
        password = request.POST.get('password')
        
        user = authenticate(username=userName, password=password)
        if user is not None:
            login(request,user)
            # A backend authenticated the credentials
            return redirect('/home')
        else:
            # No backend authenticated the credentials
            return render(request,"login.html",{"error":"Username or Passowrd is incorrect."})
    return render(request,"login.html")

def signupView(request):
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        userName = request.POST.get('userName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password==cpassword:
            user = User.objects.create_user(userName,email,password)
            user.first_name=firstName
            user.last_name=lastName
            user.save()
            return redirect('/login')
    return render(request,"signup.html")

def logoutView(request):
    logout(request)
    return redirect('/login')