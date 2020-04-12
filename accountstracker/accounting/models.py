from django.db import models
from membership.models import Member


class Transaction(models.Model):
    CURRENCY = (
        ('PHP', 'PHP'),
        ('USD', 'USD'),
        ('CAD', 'CAD'),
        ('EUR', 'EUR'),
        ('JPY', 'JPY'),
        ('AUD', 'AUD')
    )

    SERVICE = (
        ('Worship', 'Worship'),
        ('Gospel', 'Gospel'),
        ('Prayer', 'Prayer'),
        ('Other', 'Other')
    )

    member = models.ForeignKey(
        Member, blank=True, null=True, on_delete=models.SET_NULL)
    input_date = models.DateTimeField(null=True, blank=True)
    service = models.CharField(max_length=10, choices=SERVICE)
    currency = models.CharField(max_length=3, choices=CURRENCY)
    tithe = models.FloatField(null=True, blank=True)
    offering = models.FloatField(null=True, blank=True)
    firstfruit = models.FloatField(null=True, blank=True)
    firstfruit_year = models.PositiveIntegerField(blank=True, null=True)
    mission = models.FloatField(null=True, blank=True)
    care = models.FloatField(null=True, blank=True)
    ladies = models.FloatField(null=True, blank=True)
    men = models.FloatField(null=True, blank=True)
    youth = models.FloatField(null=True, blank=True)
    choir = models.FloatField(null=True, blank=True)
    prayer_breakfast = models.FloatField(null=True, blank=True)
    circle_of_faith = models.FloatField(null=True, blank=True)
    creative_team = models.FloatField(null=True, blank=True)
    dvbs = models.FloatField(null=True, blank=True)
    prison_ministry = models.FloatField(null=True, blank=True)

    others = models.FloatField(null=True, blank=True)
    others_description = models.CharField(max_length=50, null=True, blank=True)

    total = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
