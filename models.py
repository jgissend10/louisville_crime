from django.db import models

# Create your models here.
class Incident(models.Model):
    incident_date = models.DateField()
    date_reported = models.DateField()
    time_reported = models.TimeField()
    case_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    beat = models.CharField(max_length=30, blank=True)
    crime = models.CharField(max_length=30, blank=True)
    category = models.CharField(max_length=30, blank=True)
    division = models.CharField(max_length=30, blank=True)
    sector = models.CharField(max_length=30, blank=True)
    incident_beat = models.CharField(max_length=30, blank=True)
