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

    member = models.ForeignKey(
        Member, blank=True, null=True, on_delete=models.SET_NULL)
    input_date = models.DateTimeField(auto_now_add=True, null=True)

    currency = models.CharField(max_length=3, choices=CURRENCY)
    tithe = models.FloatField(default=None, null=True)
    offering = models.FloatField(default=None, null=True)
    firstfruit = models.FloatField(default=None, null=True)
    mission = models.FloatField(default=None, null=True)
    care = models.FloatField(default=None, null=True)
    ladies = models.FloatField(default=None, null=True)
    men = models.FloatField(default=None, null=True)
    youth = models.FloatField(default=None, null=True)
    choir = models.FloatField(default=None, null=True)
    prayer_breakfast = models.FloatField(default=None, null=True)
    circle_of_faith = models.FloatField(default=None, null=True)
    creative_team = models.FloatField(default=None, null=True)
    dvbs = models.FloatField(default=None, null=True)
    prison_ministry = models.FloatField(default=None, null=True)

    others = models.FloatField(default=None, null=True)
    others_description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.member
