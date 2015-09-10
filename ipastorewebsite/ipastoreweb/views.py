from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from models import Ipa


# Create your views here.

def index(request):
    latest_ipa_list = Ipa.objects.order_by('-pub_date')[:5]
    context = {'latest_ipa_list': latest_ipa_list}
    return render(request, 'ipastoreweb/index.html', context)


def detail(request, ipa_id):
    try:
        ipa = Ipa.objects.get(pk=ipa_id)
    except Ipa.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'ipastoreweb/detail.html', {'ipa': ipa})


def download(request, ipa_id):
    response = "You're looking at the results of ipa %s."
    return HttpResponse(response % ipa_id)
