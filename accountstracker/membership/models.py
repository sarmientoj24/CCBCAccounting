from django.db import models


class Member(models.Model):
    SEX = (
        ('F', 'Female'),
        ('M', 'Male')
    )

    fname = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=50, null=True)
    sex = models.CharField(max_length=1, null=True, choices=SEX)
    address = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=11, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.lname + ", " + self.fname
