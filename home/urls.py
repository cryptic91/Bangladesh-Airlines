from django.urls import path
from home import views

urlpatterns = [
    path("home/", views.home, name = "home"),
    path("about/", views.about, name = "about"),
    path("contact/", views.contact, name = "contact"),
    path("", views.login, name = "login"),
    path("signup/", views.signup, name = "signup"),
    path("showdata/", views.showdata, name = "Showdata"),
    path("logindata/", views.logindata, name = "Logindata"),
    path("signupdata/", views.signupdata, name = "Signupdata"),
    path("ticket/", views.ticket, name = "Ticket"),
]
