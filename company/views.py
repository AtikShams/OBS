from django.shortcuts import render, HttpResponse

# Create your views here.
def company_view(request):
    return HttpResponse("<h1>This is our Company page</h1>")
def cpro_view(request):
    return HttpResponse("<h1>This is our Company Profile page</h1>")
def regi_view(request):
    return HttpResponse("<h1>This is our Bus Registration page</h1>")