from django.shortcuts import render, HttpResponse, redirect



def introduce(request):
    return render(request, 'main/intro.html')