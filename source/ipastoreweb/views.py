from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the ipa-store index.")


def detail(request, ipa_id):
    return HttpResponse("You're looking at ipa %s." % ipa_id)


def download(request, ipa_id):
    response = "You're looking at the results of ipa %s."
    return HttpResponse(response % ipa_id)
