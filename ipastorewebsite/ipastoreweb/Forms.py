__author__ = 'mertsalik'

from django.forms import ModelForm
from models import Ipa
from django import forms
from validators import validate_ipa_file


class IpaUploadForm(ModelForm):
    attached_file = forms.FileField(required=True,
                                    label='Select an Ipa file',
                                    validators=[validate_ipa_file])

    class Meta:
        model = Ipa
        fields = []
