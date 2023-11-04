from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .tokens import generate_tokens
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from geostats import settings
import jwt
from datetime import datetime, timedelta


def login_page(request): 
    if not request.user.is_authenticated:
        print("Not authenticated!")     
        if request.method == 'POST':
            print("Post")
            email = request.POST['email']
            password = request.POST['psw']
         
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    print("Login Success!")
                    return redirect('/token_request')
                else:
                    messages.error(request, "Incorrect password!")
            else:
                messages.error(request, "Unknown email, please signup first!")
                return redirect('login/')

        return render(request, 'login.html')
    else:
        print("Áuthemticated")
        return HttpResponse("Hello")
    
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'logout.html')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            # Use the email's username
            username = email.split('@')[0]
            password1 = request.POST['psw']
            password2 = request.POST['psw-repeat']

            if User.objects.filter(email=email):
                messages.error(request, "Emali already registered!")
                return redirect('/signup')
                        
            if password1 != password2:
                messages.error(request, "Password didn't match!")
                return redirect('/signup')

            newuser = User.objects.create_user(username, email, password1, first_name=fname, last_name=lname)
            newuser.is_active = False
            newuser.save()

            messages.success(request, "Your Account has been successfully created.")

            return redirect('login/')
    return render(request, "signup.html")

def token_request(request):
    if request.method == 'POST':
        payload = {
            'user_id': request.user.id,
            'exp': datetime.utcnow() + timedelta(days=30)
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return render(request, 'token_display.html', {'token': token})
    return render(request, 'token_request.html')

def token_view(request):
    return render(request, 'token_display.html')

