from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

# Create your views here. 

def home (request):
    if request.method == 'POST':
        FlightNo = request.POST.get('FlightNo', None)
        Type = request.POST.get('Type', None)
        Origin = request.POST.get('Origin', None)
        Destination = request.POST.get('Destination', None)
        DepartureTime = request.POST.get('DepartureTime', None)
        ArrivalTime = request.POST.get('ArrivalTime', None)
        
        home = Ticket()
        home.FlightNo = FlightNo
        home.Type = Type
        home.Origin = Origin
        home.Destination = Destination
        home.DepartureTime = DepartureTime
        home.ArrivalTime = ArrivalTime
        home.save()
    return render(request, "home.html")

def about (request):
    return render(request, "about.html")

def contact (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        # return HttpResponse('<h1> Thanks for Contact with us</h1>')
    return render(request, "contact.html")

def login (request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # confirm = request.POST.get('confirm')
        
        login = Login()
        login.email = email
        login.password = password
        # login.confirm = confirm
        login.save()

        tultul = Signup.objects.all()
        for i in tultul:
            if i.email == email:
                if i.password == password:
                    print('Log in successfull')
                    return HttpResponseRedirect('home/')
                else:
                    print("Password doesn't match")
            else:
                print("Password doesn't match")
            
    return render(request, "login.html")

def signup (request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        presentAdd = request.POST.get('presentAdd')
        parmanentAdd = request.POST.get('parmanentAdd')
        city = request.POST.get('city')
        # district = request.POST.get('district')
        code = request.POST.get('code')
        
        signup = Signup()
        signup.firstname = firstname
        signup.lastname = lastname
        signup.email = email
        signup.password = password
        signup.presentAdd = presentAdd
        signup.parmanentAdd = parmanentAdd
        signup.city = city
        signup.code = code
        # signup.district = district
        signup.save()
    return render(request, "signup.html")

# def showdata (request):
#     return render(request, "showdata.html")

def showdata(request):
    contacts = Contact.objects.all()
    # for i in contacts:
    #     print(i.id,i.name,i.email,i.message)
    data = {'Contact':contacts}
    return render(request,'showdata.html',data)

def logindata(request):
    logins = Login.objects.all()
    # for i in contacts:
    #     print(i.id,i.name,i.email,i.message)
    data = {'Login':logins}
    return render(request,'logindata.html',data)

def signupdata(request):
    signups = Signup.objects.all()
    # for i in contacts:
    #     print(i.id,i.name,i.email,i.message)
    data = {'Signup':signups}
    return render(request,'signupdata.html',data)

def ticket(request):
    tickets = Ticket.objects.all()
    # for i in contacts:
    #     print(i.id,i.name,i.email,i.message)
    data = {'Ticket':tickets}
    return render(request,'ticket.html',data)
