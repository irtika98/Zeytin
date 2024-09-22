from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone

from .pipeline.RAG import RAG
rag = RAG()

def invoke(message):
    
    response = rag.get_response(message)
    print(response)
    return response

def chat(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        query = request.POST.get('message')
        response = invoke(query)

        chat = Chat(user=request.user, query=query, response=response, time=timezone.now())
        chat.save()
        return JsonResponse({'message': query, 'response': response})
    return render(request, 'chatbot.html', {'chats': chats})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chat')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if confirm_password == password:
            try:
                user = User.objects.create_user(username, email, password)
                print('hello')
                user.save()
                auth.login(request, user)
                return redirect('chat')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
