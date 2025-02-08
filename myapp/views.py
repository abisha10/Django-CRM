from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def Home(request):
    # check if the user is logged in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('myapp:home')
        else:
            messages.success(request, "There is an error logging in. Please provide correct username and password!")
            return redirect('myapp:home')
    else:
        return render(request, 'home.html')

# def Login(request):
#     pass

def Logout(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('myapp:home')

def Register(request):
    

    return render(request, 'register.html')