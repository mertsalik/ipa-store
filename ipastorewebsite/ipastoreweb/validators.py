__author__ = 'mertsalik'

from django.core.exceptions import ValidationError


def validate_ipa_file(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    print "ext %s", ext
    valid_extensions = ['.ipa', ]
    if not ext in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')
