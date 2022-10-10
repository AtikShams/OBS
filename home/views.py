from django.shortcuts import render, HttpResponse

# Create your views here.
def landing(request):
        return render(request, 'landing.html')

def homepage(request):
        return render(request, 'homepage.html')

def about_us(request):
        return render(request, 'about_us.html')


def contact_us(request):
        return render(request, 'contact_us.html')

def term_and_condition(request):
        return render(request, 't&c.html')

def faq(request):
        return render(request, 'faq.html')
def homepage_admin(request):
        return render(request, 'homepage_admin.html')
