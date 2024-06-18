from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.shortcuts import render
from django.contrib import auth
from users.forms import UserSigninForm

class UserSigninView(View):
    def post(self, request):
        if request.method == "POST":
            form = UserSigninForm(data=request.POST)
            if form.is_valid():
                username = request.POST["username"]
                password = request.POST["password"]
                user = auth.authenticate(username=username, password=password)
                if user:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse("user:profile"))
        else:
            form = UserSigninForm()
        
        context = {
            "form": form,
        }
        return render(request, "users/signin.html", context)
    
    def get(self, request):
        form = UserSigninForm()
        context = {
            "form": form,
        }
        return render(request, "users/signin.html", context)

class UserSignupView(View):
    def get(self, request):
        return render(request, "users/signup.html")

class UserForgotView(View):
    def get(self, request):
        return render(request, "users/forgot.html")

class UserSignoutView(View):
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse("users:signin"))

class UserProfileView(View):
    def get(self, request):
        return render(request, "users/profile.html")