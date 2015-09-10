from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.http import HttpResponseBadRequest
from django.http import HttpResponseServerError
from django.core.urlresolvers import reverse
from models import Ipa
from forms import IpaUploadForm
import os
import uuid
import datetime

IPA_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "static")


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


def delete(request, ipa_id):
    response = "You're deleting ipa %s."
    return HttpResponse(response % ipa_id)


def upload(request):
    if request.method == 'POST':
        form = IpaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                ipa_path = handle_uploaded_file(request.FILES['attached_file'])
                ipa_model = form.save(commit=False)
                ipa_model.file_path = ipa_path
                ipa_model.save()
            except Exception as e:
                return HttpResponseServerError(
                    "An error occured while saving ipa file")

            return HttpResponseRedirect(reverse('ipastoreweb.views.index'))
        else:
            context = {'form': form}
            return render_to_response('ipastoreweb/upload.html', context)
    else:
        context = {'form': IpaUploadForm()}
        return render(request, 'ipastoreweb/upload.html', context)


def handle_uploaded_file(f):
    if f:
        filename = uuid.uuid4().hex[:6].upper()
        destination_path = "{}/{}.ipa".format(IPA_FOLDER, filename)
        try:
            with open(destination_path, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        except IOError as ioe:
            raise HttpResponseServerError(ioe.message)
        return destination_path
    else:
        raise HttpResponseBadRequest("Empty or null file given")
