from django.shortcuts import render, HttpResponse,reverse,redirect
from django.http import HttpRequest, Http404, HttpResponseRedirect


def auth(request):
    if request.method == "GET":
        return render(request, 'main/auth.html', status=200)
    else:
        if 'name' in request.POST:
            request.session['name'] = request.POST['name']
            request.session.save()
            return HttpResponseRedirect(redirect_to=reverse("home"))
        else:
            return Http404