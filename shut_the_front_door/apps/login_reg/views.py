from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.
# VIEWS FOR LOGIN_REG APP

@xframe_options_exempt
def index(request):
    return render(request, "login_reg/login.html")

# this method will create a new user
# route views.create
def create(request):
    errors = User.objects.basic_validator(request.POST)
    # check if user fails the registration validators
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/show_register")
    else:
        pw = request.POST['password']
        hashed_pw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        User.objects.basic_validator(request.POST)
        User.objects.create(first_name=request.POST['first_name'],
                            last_name=request.POST['last_name'],
                            email=request.POST['email'],
                            password=hashed_pw.decode())
        user = User.objects.get(email=request.POST['email'])
        # storing the user.id in session
        request.session['user_id'] = user.id
        messages.success(request, "User successfully added!")
        # make sure to redirect to after reg or login to profile
        return redirect("/filter")

@xframe_options_exempt
def show_register(request):
    return render(request, "login_reg/register.html")

# this method will route to logged in page
# route views.success
def success(request):
    # check to see if user is still in session
    if 'user_id' not in request.session:
        messages.error(request, "Please login!")
        return redirect("/")
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user
            }
        return redirect("/filter") # change redirect here

# this method will allow a user to login
# route views.login
def login(request):
    errors = User.objects.login_validator(request.POST)
    # check if user fails the registration validators
    if len(errors) > 0:
        print("errors")
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        messages.success(request, "User successfully logged in!")
        # make sure to redirect to after reg or login to profile
        return redirect("/filter")

# this method will log the user out and clear all session keys
# route views.logout
def logout(request):
    request.session.clear()
    messages.success(request, "User successfully logged out!")
    return redirect("/")