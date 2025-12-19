from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login,logout

# Create your views here.
def index(req):
    return render(req,'index.html')

def dashboard(req):
    if req.user.is_authenticated:
        return render (req,'dashboard.html')
    else:
        return redirect('login')
def login_html(req):
    return render(req,'login.html')

def login_page(req):
    if req.method=='POST':
        email=req.POST.get("email")
        parol=req.POST.get("password")
        print(email,parol)
        user=authenticate(req,username=email,password=parol)
        
        if user is not None:
            login(req,user)
            return redirect ("dashboard")        
    return redirect("login")

def logoutp_page(req):
    if req.user.is_authenticated:
        logout(req)
    return redirect ("login")

def quiz_page(req):
    return render(req,'quiz_page.html')

def result(req):
    return render (req,'result.html')


def settings(req):
    return render(req,'settings.html')