from django.contrib import admin
from django.urls import path
from url import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('u/<slug:short_url>', views.shorten, name='shorten'),
    path('new', views.url, name='new'),
    path('', views.home, name='home'),
]
