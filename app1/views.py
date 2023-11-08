from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def JamPandu(request):
    return HttpResponse('<h1><marquee>Hi</marquee></h1>')

def JigelRani(request):
    return HttpResponse('<h1><marquee>Hello</marquee></h1>')