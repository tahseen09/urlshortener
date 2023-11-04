from django.contrib import admin
from django.urls import path, include
from url import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('u/<slug:short_url>', views.shorten, name='short'),
    path('url/<slug:short_url>', views.url, name='url_update'),
    path('url', views.url, name='url'),
    path('accounts/signup', views.signup, name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
]
