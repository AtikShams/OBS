from django.shortcuts import render,HttpResponse

# Create your views here.
def passenger_view(request):
    return render(request,'pas-view.html')
def passenger_profile_view(request):
    return render(request,'pas-view.html')
def purchase_ticket_view(request):
    return render(request,'pas-view.html')
def payment_view(request):
    return render(request,'pas-view.html')
def bus_schedule_view(request):
    return render(request,'pas-view.html')
def sunlight_direction_view(request):
    return render(request,'pas-view.html')
def bus_tracking_view(request):
    return render(request,'pas-view.html')
def bus_reservation_view(request):
    return render(request,'pas-view.html')
