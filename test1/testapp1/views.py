from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth


#form django.views.decorators.cache import cache_control



def index(request):
    if request.method == 'POST':
        sbid = request.POST['id']
        password = request.POST['psd']

        user = auth.authenticate(username=sbid,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("home/")
        else:
            messages.info(request,'Username or password invalid')
            return redirect("/")

    else:
        return render(request,'index.html')


def home(request):
    return render(request,'home.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect("/")


def addclient(request):
    if request.method == 'POST':
        name = request.POST['name']
        compnyname = request.POST['compenyName']
        email = request.POST['email']
        contect_number = request.POST['number']
        address = request.POST['address']
        #country = request.POST['country']
        city = request.POST['city']
        client = Client(clientname=name,compenyname=compnyname,email=email,phone=contect_number,address=address,clientcity = city)
        client.save()
        return render(request,'home.html')

    else:
        #citie = cities_light.models.City.objects.all()
        #citi = Client.objects.all()
        #contry = cities_light.models.Country.objects.all()
        return render(request, 'addClient.html')


def addequepment(request):
    if request.method == 'POST':
        return render(request,'addequepment.html')
    else:

        return render(request, 'addequepment.html')


def addplant(request):
    if request.method == 'POST':
        return render(request,'addplant.html')
    else:
        return render(request, 'addplant.html')


def addproject(request):
    if request.method == 'POST':
        return render(request,'addproject.html')
    else:
        return render(request, 'addproject.html')


def addwherehouse(request):
    if request.method == 'POST':
        return render(request,'addwherehouse.html')
    else:
        return render(request, 'addwherehouse.html')


def vclient(request):
    if request.method == 'POST':
        # role1 = role.objects.all()
        # print(role1)
        return render(request,'vclient.html')
    else:
        role1 = Client.objects.all()
        print(role1)
        return render(request, 'vclient.html',{'role1': role1})


def vequepment(request):
    if request.method == 'POST':

        return render(request,'vequepment.html')
    else:
        #e1 = EquepmentMaster.objects.all()
        equepmentdata = Equepmentdetails.objects.all()
        return render(request, 'vequepment.html',{'ed':equepmentdata})


def vplant(request):
    if request.method == 'POST':
        return render(request,'vplant.html')
    else:
        plantdata = Plant.objects.all()
        return render(request, 'vplant.html',{'pd':plantdata})


def vproject(request):
    if request.method == 'POST':
        return render(request,'vproject.html')
    else:
        projectdata = Project.objects.all()
        return render(request, 'vproject.html',{'pd':projectdata})



def vwherehouse(request):
    if request.method == 'POST':
        return render(request,'vwherehouse.html')
    else:
        werehousedata = Warehouse.objects.all()
        return render(request,'vwherehouse.html',{'wh':werehousedata})

