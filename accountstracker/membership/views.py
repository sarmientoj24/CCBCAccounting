from django.shortcuts import render
from .models import Member


def members(request):
    members = Member.objects.all()
    return render(request, 'membership/membership.html', {'members': members})
