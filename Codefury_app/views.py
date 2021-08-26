from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'home.html', {"form": form})
