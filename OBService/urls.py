"""OBService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.SignUp_Login, name='SignUp_Login')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='SignUp_Login')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import SignUp_Login.views as h
import passenger.views as pa
import company.views as co
import admin.views as ad
urlpatterns = [
    path('admin/', admin.site.urls),
    #Home App
    path('landing/', home.views.landing),
    path('homepage/', home.views.homepage),
    path('contact_us/', home.views.contact_us),
    path('about_us/', home.views.about_us),
    path('Term_and_condition/', home.views.term_and_condition),
    path('faq/', home.views.faq),
    path('homepage_admin/', home.views.homepage_admin),


    #SignUp/Login App
    path('sign_up_op/',h.signupop_view ),
    path('signup_passenger/',h.signuppassenger_view ),
    path('signup_company/',h.signupcompany_view ),
    path('login/',h.login_view ),

    #Company App
    path('company/', co.company_view),
    path('cpro/', co.cpro_view),
    path('registraton/', co.regi_view),

    #Passenger App

    path('bus_reservation/', pas.bus_reservation_view),
    path('passenger_profile/', pas.passenger_profile_view),
    path('payment/', pas.payment_view),
    path('purchase_ticket/', pas.purchase_ticket_view),
    path('sunlight_direction/', pas.sunlight_direction_view),
    path('bus_schedule/', pas.bus_schedule_view),
    path('bus_tracking/', pas.bus_tracking_view),
    path('term_and_condition/', pas.term_and_condition_view),





]
