from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, AddRecordForm
from .models import Record

# Create your views here.
def Home(request):
    records = Record.objects.all()



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
        return render(request, 'home.html', {'records':records})  #{'records':records} means we passing the models to template

# def Login(request):
#     pass

def Logout(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('myapp:home')

def Register(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('myapp:home')
	else:
		form = SignupForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def Customer_Record(request,pk):
      customer_record = Record.objects.get(id=pk)
      return render(request, 'record.html', {'customer_record':customer_record})

def Delete_Record(request, pk):
    delete_record = Record.objects.get(id=pk)
    delete_record.delete()
    messages.success(request, "Record has been deleted!")
    return redirect('myapp:home')

def Add_Record(request):
    form = AddRecordForm(request.POST or None)
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been added!")
            return redirect('myapp:home')
    else:
        form = AddRecordForm()

    return render(request, 'add_record.html',{'form':form})

def Update(request,pk):
     current_record = Record.objects.get(id=pk)
     form = AddRecordForm(request.POST or None, instance=current_record)
     if form.is_valid():
          form.save()
          messages.success(request,"Record Updated Successfully!")
          return redirect('myapp:home')
     return render(request,"update.html",{'form':form})

     