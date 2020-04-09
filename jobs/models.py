from django.db import models
from datetime import date
# Create your models here.

class Job(models.Model):
    query = models.CharField(max_length=255, blank=True)
    href = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    cn = models.CharField(max_length=255, blank=True)
    crv = models.CharField(max_length=255, blank=True)
    crc = models.CharField(max_length=255, blank=True)
    loc = models.CharField(max_length=255, blank=True)
    metaheader = models.CharField(max_length=255, blank=True)
    desc = models.TextField(blank=True)
    date = models.DateField(default=date.today)


class Query(models.Model):
    query = models.CharField(max_length=255, blank=True)
