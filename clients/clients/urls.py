from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect('/clients/')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('clients/', include('clients_manager.urls')),
    path('login/', include("login.urls")),
]