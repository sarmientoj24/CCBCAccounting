from django.db import models


class Member(models.Model):
    SEX = (
        ('F', 'Female'),
        ('M', 'Male')
    )

    MEMBER = (
        ('Member', 'Member'),
        ('Visitor', 'Visitor')
    )

    STATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Separated', 'Separated'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed')
    )

    fname = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    mname = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(
        max_length=1, blank=True, null=True, choices=SEX, default='M')
    is_member = models.CharField(
        max_length=8, null=True, choices=MEMBER)
    bdate = models.DateTimeField(null=True, blank=True)
    bdate_place = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    civilstatus = models.CharField(
        max_length=10, null=True, blank=True, choices=STATUS, default='Single')
    spouse = models.CharField(max_length=50, null=True, blank=True)
    spouse_occupation = models.CharField(max_length=50, null=True, blank=True)
    date_of_marriage = models.DateTimeField(null=True, blank=True)
    father = models.CharField(max_length=50, null=True, blank=True)
    father_occupation = models.CharField(max_length=50, null=True, blank=True)
    mother = models.CharField(max_length=50, null=True, blank=True)
    mother_occupation = models.CharField(max_length=50, null=True, blank=True)
    children = models.CharField(max_length=200, null=True, blank=True)
    elementary = models.CharField(max_length=50, null=True, blank=True)
    elementary_year = models.IntegerField(blank=True, null=True)
    highschool = models.CharField(max_length=50, null=True, blank=True)
    highschool_year = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=50, null=True, blank=True)
    course = models.CharField(max_length=50, null=True, blank=True)
    college_year = models.IntegerField(blank=True, null=True)
    date_of_salvation = models.DateTimeField(null=True, blank=True)
    date_baptized = models.DateTimeField(null=True, blank=True)
    place_baptized = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        if self.lname is None:
            return self.fname
        return self.lname + ", " + self.fname
