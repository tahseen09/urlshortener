from django.contrib import admin
from django.urls import path
from url import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', csrf_exempt(views.index), name='index'),
    path('<slug:short_url>', views.shorten, name='shorten'),
]
