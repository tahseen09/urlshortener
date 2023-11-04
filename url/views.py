from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from .models import Link
from .services import generate_short_url


@login_required
def home(request):
    urls = Link.objects.filter(user=request.user)
    context = {"urls": urls}
    return render(request, "home.html", context)


def _create(url: str, user: User) -> Link:
    short_url = generate_short_url()
    link = Link(og=url, short=short_url, user=user)
    link.save()
    return link


def _update(url: str, short_url: str, user: User) -> Link:
    link = Link.objects.get(short=short_url, user=user)
    link.og = url
    link.save()
    return link


@login_required
def url(request, short_url=None):
    if request.method == "POST":
        url = request.POST.get("url")
        link = _update(url, short_url, request.user) if short_url else _create(url, request.user)
        return redirect("home")

    og = ""
    if short_url:
        link = Link.objects.get(short=short_url)
        og = link.og
    return render(request, "url.html", context={"og": og})


def shorten(request, short_url=""):
    try:
        u = Link.objects.get(short=short_url)
    except Link.DoesNotExist:
        return HttpResponse("URL Not Found")
    else:
        u.visit_count += 1
        u.save()
    return redirect(u.og)


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User(username=username, email=username, password=make_password(password))
        user.save()
        return redirect("login")

    return render(request, "registration/signup.html")
