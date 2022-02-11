from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .forms import CustomRegistrationForm

# Create your views here.

def register(request):
    # return render(request, "")

    if request.method == 'POST':
        registerForm = CustomRegistrationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            messages.success(request, 'New User Account Created')
        return render(request, 'register.html', {'registerForm': registerForm})

    else:
        registerForm = CustomRegistrationForm()
        return render(request, 'register.html', {'registerForm': registerForm})