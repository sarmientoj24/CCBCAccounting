from django.db import models
from membership.models import Member


class Expenses(models.Model):
    CATEGORIES = (
        ('others', 'others'),
        ('allowances', 'allowances'),
        ('utilities', 'utilities'),
        ('cash advance', 'cash advance'),
        ('mission', 'mission'),
        ('care', 'care'),
        ('ladies', 'ladies'),
        ('men', 'men'),
        ('ladies', 'ladies'),
        ('youth', 'youth'),
        ('prayer_breakfast', 'prayer_breakfast'),
        ('circle_of_faith', 'circle_of_faith'),
        ('creative_team', 'creative_team'),
        ('dvbs', 'dvbs'),
        ('prison_ministry', 'prison_ministry'),
        ('tithe', 'tithe'),
        ('offering', 'offering'),
        ('firstfruit', 'firstfruit')
    )

    member = models.ForeignKey(
        Member, blank=True, null=True, on_delete=models.SET_NULL)
    input_date = models.DateTimeField(auto_now_add=True, null=True)

    serial = models.CharField(max_length=50, null=True)
    amount = models.FloatField(default=0)
    category = models.CharField(max_length=20, null=True, choices=CATEGORIES)
    description = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.serial + " " + self.category
