from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)  # Ensure 'user' is passed here
            return redirect("home")  # Redirect to 'home' page after login
        else:
            error_message = "Invalid username or password."
    return render(request, "login.html", {"error_message": error_message})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def surprise(request):
    return render(request, 'surprise.html')
