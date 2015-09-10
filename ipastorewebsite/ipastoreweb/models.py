from django.db import models


# Create your models here.
class Ipa(models.Model):
    id = models.IntegerField('Identifier', primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    app_version = models.CharField(max_length=20)
    pub_date = models.DateTimeField('Date Published', auto_now_add=True)
    download_count = models.PositiveSmallIntegerField('Download Count',
                                                      default=0)
    file_path = models.CharField(max_length=500)
