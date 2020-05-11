from django.db import models
from membership.models import Member
from datetime import date


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

    today = date.today()
    today_date = today.strftime("%Y-%m-%d")
    today_year = today.strftime("%Y")

    member = models.ForeignKey(
        Member, blank=True, null=True, on_delete=models.SET_NULL)
    input_date = models.DateField(default=today_date, blank=True)
    service = models.CharField(max_length=10, choices=SERVICE)
    currency = models.CharField(max_length=3, choices=CURRENCY)
    tithe = models.FloatField(blank=True, null=True)
    offering = models.FloatField(blank=True, null=True)
    firstfruit = models.FloatField(blank=True, null=True)
    firstfruit_year = models.PositiveIntegerField(
        blank=True, default=today_year)
    mission = models.FloatField(blank=True, null=True)
    care = models.FloatField(blank=True, null=True)
    ladies = models.FloatField(blank=True, null=True)
    men = models.FloatField(blank=True, null=True)
    youth = models.FloatField(blank=True, null=True)
    choir = models.FloatField(blank=True, null=True)
    prayer_breakfast = models.FloatField(blank=True, null=True)
    circle_of_faith = models.FloatField(blank=True, null=True)
    creative_team = models.FloatField(blank=True, null=True)
    dvbs = models.FloatField(blank=True, null=True)
    prison_ministry = models.FloatField(blank=True, null=True)

    others = models.FloatField(blank=True, null=True)
    others_description = models.CharField(max_length=50, null=True, blank=True)

    total = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.id)
