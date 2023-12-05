from django.shortcuts import render, HttpResponse


def about(request):
    return render(request, "about.html")


def home(request):
    return render(request, "home.html")
