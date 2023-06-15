from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from cryptography.fernet import Fernet
from mechanize import Browser
from .models import Password
import random
import favicon

br = Browser()
br.set_handle_robots(False)
fernet = Fernet(settings.KEY)

def home(request):
    if request.method == "POST":
        if "signup-form" in request.POST:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            password2 = request.POST.get("password2")
            # check if passwords are same
            if password != password2:
                msg = "Passwords MUST be NOT identical!!"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)
            # handle existing usernames
            elif User.objects.filter(username=username).exists():
                msg = f"{username} already exists!!"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)
            # handle existing email
            elif User.objects.filter(email=email).exists():
                msg = f"{email} already exists!!"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)
            # else create user and login in
            else:
                new_user = User.objects.create_user(email=email, username=username, password=password2)
                if new_user is not None:
                    msg = f"{username} registered successfully :) "
                    messages.success(request, msg)
                    return HttpResponseRedirect(request.path)
        
        elif "logout" in request.POST:
            logout(request)
            msg = f"Logged out successfully!!"
            messages.success(request, msg)
            return HttpResponseRedirect(request.path)
        
        elif "login-form" in request.POST: #(repair login form)
            username = request.POST.get("username")
            password = request.POST.get("password")
            new_login = authenticate(request, username=username, password=password)
            if new_login is None:
                msg = f"username or password incorrect"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)
            else:
                """code = str(random.randint(100000, 999999))
                global global_code
                global_code = code
                send_mail(
                    "badpass : confirm your OTP",
                    f"Your OTP is {code}.",
                    settings.EMAIL_HOST_USER,
                    [new_login.email],
                    fail_silently=False
                )
                return render(request, "index.html",{
                    "code":code,
                    "user":new_login,
                })
        
        if "confirm" in request.POST:
            user_code = request.POST.get("code")
            user = request.POST.get("user")
            #global global_code
            if user_code != global_code:
                msg = f"incorrect code!!"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)
            else:"""
                #for confirmation code, uncomment, change the following line to : login(request, User.objects.get(username=user))
                login(request, User.objects.get(username=username))
                msg = f"welcome back {request.user}."
                messages.success(request, msg)
                return HttpResponseRedirect(request.path)
        
        elif "add-password" in request.POST:
            url = request.POST.get("url")
            email = request.POST.get("email")
            password = request.POST.get("password")
            # encrypt email and password
            encrypted_email = fernet.encrypt(email.encode())
            encrypted_password = fernet.encrypt(password.encode())
            # get title of website
            br.open(url)
            title = br.title()
            # get logo of a website
            icon = favicon.get(url)[0].url
            # save data
            new_password = Password.objects.create(
                user = request.user,
                name=title,
                logo=icon,
                email=encrypted_email.decode(),
                password=encrypted_password.decode(),
            )
            msg = f"{title} added successfully!!"
            messages.success(request, msg)
            return HttpResponseRedirect(request.path)
        
        elif "delete" in request.POST:
            to_be_deleted = request.POST.get("password-id")
            msg = f"{Password.objects.get(id=to_be_deleted)} deleted successfully!!"
            Password.objects.get(id=to_be_deleted).delete()
            messages.success(request, msg)
            return HttpResponseRedirect(request.path)

    context = {}
    if request.user.is_authenticated:
        passwords = Password.objects.all().filter(user=request.user)
        for password in passwords:
            password.email = fernet.decrypt(password.email.encode()).decode()
            password.password = fernet.decrypt(password.password.encode()).decode()
        context = {
            "passwords":passwords,
        }
    """else:
        return render(request, "home.html", {})"""


    return render(request, "index.html", context)