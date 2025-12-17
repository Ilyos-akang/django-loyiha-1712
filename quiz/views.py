from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')

def dashboard(req):
    return render (req,'dashboard.html')

def login(req):
    return render(req,'login.html')

def quiz_page(req):
    return render(req,'quiz_page.html')

def result(req):
    return render (req,'result.html')


def settings(req):
    return render(req,'settings.html')