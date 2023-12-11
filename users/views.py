from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .tokens import account_activation_token
from .models import Profile
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            token = str(account_activation_token.make_token(user))
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get("email")
            p = Profile.objects.create(
                auth_token=token,
                username=username,
                email=email,
                password=password,
                is_verified=False,
            )
            p.save()
            sender = settings.EMAIL_HOST_USER
            print(sender)
            subject = "Your account needs to be verified"
            message = f"Hi click on this link to verify your account http://127.0.0.1:8000/verify/{token}"
            recipient_list = [email]
            send_mail(subject, message, sender, recipient_list)
            return render(request, "users/token_send.html", {})
        else:
            return redirect("/error")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def verify(request, auth_token):
    profile_obj = Profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        profile_obj.is_verified = True
        profile_obj.save()
        user = User.objects.create(
            username=profile_obj.username, email=profile_obj.email
        )
        user.set_password(profile_obj.password)
        user.save()
        messages.info(request, "Your account has been verified")
        return redirect("/login")
    else:
        return redirect("/error")


def error_page(request):
    return render(request, "users/error.html", {})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "users/profile.html", context)
