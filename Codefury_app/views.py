from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
from Codefury_app.models import Announcment, Question
from django.shortcuts import *
from django.template import RequestContext


# Create your views here.

@csrf_exempt
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ContactForm()
            faqs = Question.objects.all()
            announcements = Announcment.objects.all().order_by('date').order_by('time')
            message="Thank You! for writing to us. We will get back to you shortly"
            return render(request, 'home.html', {"form": form, 'faqs':faqs, 'announcements':announcements,"message":message})

    else:
        form = ContactForm()
        faqs = Question.objects.all()
        announcements = Announcment.objects.all().order_by('date').order_by('time')
    return render(request, 'home.html', {"form": form, 'faqs':faqs, 'announcements':announcements})
