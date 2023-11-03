from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Link
from .services import generate_short_url


def home(request):
    urls = Link.objects.all()
    context = {"urls": urls}
    return render(request, "home.html", context)

def _create_new(url: str) -> str:
    short_url = generate_short_url()
    link = Link(og=url, short=short_url)
    link.save()
    return short_url


def url(request):
    if request.method == "POST":
        url = request.POST.get("url")
        short_url = _create_new(url)
        return redirect("home")

    return render(request, "url.html")

def shorten(request, short_url=""):
    try:
        u = Link.objects.get(short=short_url)
    except Link.DoesNotExist:
        return HttpResponse("URL Not Found")
    else:
        u.visit_count += 1
        u.save()
    return redirect(u.og)
