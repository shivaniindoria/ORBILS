# from django.shortcuts import render
from django.http.response import HttpResponse


def IndexView(request):
    return HttpResponse("welcome to Orbils")
