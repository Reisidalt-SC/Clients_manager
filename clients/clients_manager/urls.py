from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_creation, name='home'),
    path('client_creation/', views.client_creation, name='client_creation'),
    path('client_delete/<int:id>/', views.client_delete, name='client_delete'),
    path('client_update/<int:id>/', views.client_update, name='client_update'),
    path('client_finish/<int:id>/', views.client_finish, name='client_finish'),
    path('finished_clients/', views.finished_clients, name='finished_clients'),
     path('logout/', views.user_logout, name='logout'),
]