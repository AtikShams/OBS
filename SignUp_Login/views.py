from django.shortcuts import render, HttpResponse

# Create your views here.

def signupop_view(request):
    return HttpResponse("<h1>This is our SignUp option page</h1>")
def signuppassenger_view(request):
    return HttpResponse("<h1>This is our SignUp as passenger page</h1>")
def signupcompany_view(request):
    return HttpResponse("<h1>This is our SignUp as company page</h1>")
def login_view(request):
    return HttpResponse("<h1>This is our Login page</h1>")
