from django.shortcuts import render, HttpResponse,reverse,redirect
from django.http import HttpRequest, Http404, HttpResponseRedirect
from .models import Message

def send_message(request):
    name = request.session['name']
    content = request.POST['content']
    payload = {'name': name, 'content': content}
    #print(f"got message: {payload}")
    message = Message.objects.create(name=name, content=content)
    message.save()
    #print(f"message: {payload} saved")
    return redirect(reverse('home'))

def homepage(request):
    if 'name' in request.session:
        #name = request.GET['name']
        messages = []
        for message in Message.objects.all():
            messages.append({'info': f"{message.name} {str(message.timestamp)[:-16]}:", 'content': message.content})
        #print(f"messages: {messages}")
        name = request.session["name"]
        return render(request, 'main/home.html', {'name': name, "messages": messages})
    return redirect('/')
