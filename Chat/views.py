from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from .models import Message
import json

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=username+"@gmail.com", password=password)
        user.save()
        user=authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        return render(request, 'login.html')
    return render(request, 'login.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

def index(request):
    if request.user.is_authenticated:
        sent_messages = Message.objects.filter(Sender=request.user).values_list('Reciever', flat=True)
        received_messages = Message.objects.filter(Reciever=request.user).values_list('Sender', flat=True)
        
        # Combine the user IDs from both querysets and get distinct users
        user_ids = list(set(sent_messages) | set(received_messages))
        users_with_messages = User.objects.filter(id__in=user_ids)
        return render(request, 'index.html', {
            'users': users_with_messages
        })
    else:
        return redirect('login')

def loadchat_view(request):
    if request.user.is_authenticated and request.method=="POST":
        data = json.loads(request.body)
        print(data)
        sender = request.user
        receiver = User.objects.get(id=data['reciever_id'])
        sent_messages = Message.objects.filter(Sender=sender, Reciever=receiver)

        # Get messages received by sender from receiver (if you want both directions)
        received_messages = Message.objects.filter(Sender=receiver, Reciever=sender)
        # Combine the two querysets if you want all messages between the two users
        all_messages = sent_messages | received_messages

        # Optionally, you can order the combined messages by message_time
        messages = all_messages.order_by('message_time').values()
        return JsonResponse({
            'messages' : list(messages)
            })
    else:
        return redirect('login')