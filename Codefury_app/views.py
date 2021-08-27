from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
from Codefury_app.models import Announcment, Question
# Create your views here.

@csrf_exempt
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()
        faqs = Question.objects.all()
        announcements = Announcment.objects.all().order_by('date').order_by('time')
    return render(request, 'home.html', {"form": form, 'faqs':faqs, 'announcements':announcements})
