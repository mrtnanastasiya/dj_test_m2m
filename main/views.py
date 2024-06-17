from django.shortcuts import render, redirect
from main.models import User, Service, Subscription

def homepage(request):
    template = 'homepage.html'
    context = {'service_list': Service.objects.all()}
    return render(request, template, context)

def service(request, name):
    template = 'service.html'
    context = {}
    return render(request, template, context)

