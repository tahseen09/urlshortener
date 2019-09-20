from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponsePermanentRedirect
from .models import url_db
from urlshortener import urls
from django.urls import path
from . import views


def index(request):
    if request.method == "POST":
        og_url = request.POST.get("og_url")
        short_url = request.POST.get("short_url")
        url_db(og=og_url, short=short_url).save()
        return HttpResponse("Your new URL is " + short_url)


def shorten(request, short_url=""):
    short_url = str(request.get_full_path())[1:]
    u = url_db.objects.get(short=short_url)
    return redirect(u.og)
