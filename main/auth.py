from django.shortcuts import render, HttpResponse,reverse,redirect
from django.http import HttpRequest, Http404, HttpResponseRedirect
from .models import Name


def auth(request):
    if request.method == "GET":
        return render(request, 'main/auth.html', status=200)
    else:
        if 'name' in request.POST:
            name = request.POST['name']
            request.session['name'] = name

            try:
                new_name = Name.objects.create(name=name)
                new_name.save()
            except:
                pass

            request.session.save()
            return HttpResponseRedirect(redirect_to=reverse("home"))
        else:
            return Http404