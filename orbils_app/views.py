from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def IndexView(request):
    return HttpResponse("welcome to Orbils")
