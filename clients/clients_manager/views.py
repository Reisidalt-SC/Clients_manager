from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Finishedclient
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def client_creation(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        return render(request, 'clients_creation.html', {'clients': clients})

    elif request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        tel = request.POST.get('tel', '').strip()
        city = request.POST.get('city', '').strip()
        packet = request.POST.get('packet', '').strip()
        message = request.POST.get('message', '').strip()

        # empty field validation
        for field_name, value in [('Name', name), ('Email', email), ('Tel', tel), 
                                  ('City', city), ('Packet', packet), ('Message', message)]:
            if not value:
                return render(request, 'clients_creation.html', {
                    'error_message': f'{field_name} vazio',
                    'clients': Client.objects.all()
                })

        # client creation
        client = Client(
            name=name, 
            email=email, 
            tel=tel, 
            city=city, 
            packet=packet, 
            message=message
        )
        client.save()
        return redirect('client_creation')
    
def finished_clients(request):
    finished_clients = Finishedclient.objects.all()
    return render(request, 'finished_clients.html', {'finished_clients': finished_clients})   


def client_delete(request, id):
    client = get_object_or_404(Client, id=id)
    client.delete()
    return redirect('client_creation')

def client_update(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        client.name = request.POST.get('name')
        client.email = request.POST.get('email')
        client.tel = request.POST.get('tel')
        client.city = request.POST.get('city')
        client.packet = request.POST.get('packet')
        client.message = request.POST.get('message')
        client.save()
        return redirect('client_creation')
    

def client_finish(request, id):
    client = get_object_or_404(Client, id=id)
    
    finished_client = Finishedclient(
        name=client.name,
        email=client.email,
        tel=client.tel,
        city=client.city,
        packet=client.packet,
        message=client.message
    )
    finished_client.save()
    client.delete()
    return redirect('client_creation')


def user_logout(request):
    logout(request)
    return redirect('login')

