from django.db import models

# Create your models here.

class Donation(models.Model):
    donation_date = models.DateField(null=True)
    systolic = models.IntegerField(null=True)
    diastolic = models.IntegerField(null=True)
    donation_center = models.CharField(max_length=20)
    donation_type = models.CharField(max_length=10)

    def __unicode__(self):
        if not self.donation_date:
            return 'no donation date'
        else:
            return str(self.donation_date)

    def has_date(self):
        if donation_date:
            return true
        else:
            return false
    def has_blood_pressure(self):
        if systolic and diastolic:
            return true
        else:
            return false
    def units_donated(self):
        if donation_type == "DRB":
            return 2
        else:
            return 1
