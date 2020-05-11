from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from accounting.models import Transaction
from accounting.forms import TransactionForm
import datetime


def members(request):
    members = Member.objects.all()
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    members_today = Member.objects.filter(date_created__gt=yesterday)

    context = {
        'members': members,
        'members_count': len(members),
        'created_today_count': len(members_today)
    }

    return render(request, 'membership/membership.html', context)


def profile(request, pk):
    member = Member.objects.get(id=pk)
    context = {'member': member}
    context['fullname'] = member.fname.upper() + " " + member.lname.upper()
    return render(request, 'membership/profile.html', context)


def add_transaction(request, pk):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        print(form.errors)

        if form.is_valid():
            try:
                member = Member.objects.get(id=pk)
                instance = form.save(commit=False)
                instance.member = member
                instance.tithe = instance.tithe if instance.tithe is not None else 0
                instance.offering = instance.offering if instance.offering is not None else 0
                instance.firstfruit = instance.firstfruit if instance.firstfruit is not None else 0
                instance.mission = instance.mission if instance.mission is not None else 0
                instance.care = instance.care if instance.care is not None else 0
                instance.ladies = instance.ladies if instance.ladies is not None else 0
                instance.men = instance.men if instance.men is not None else 0
                instance.youth = instance.youth if instance.youth is not None else 0
                instance.choir = instance.choir if instance.choir is not None else 0
                instance.prayer_breakfast = instance.prayer_breakfast if instance.prayer_breakfast is not None else 0
                instance.circle_of_faith = instance.circle_of_faith if instance.circle_of_faith is not None else 0
                instance.creative_team = instance.creative_team if instance.creative_team is not None else 0
                instance.dvbs = instance.dvbs if instance.dvbs is not None else 0
                instance.prison_ministry = instance.prison_ministry if instance.prison_ministry is not None else 0
                instance.others = instance.others if instance.others is not None else 0

                if instance.total is not None and instance.total > 0:
                    instance.save()
                return redirect('/membership')
            except:
                pass
    return redirect('/membership')


def delete_member(request, pk):
    member = Member.objects.get(id=pk)
    if request.method == 'POST':
        try:
            member.delete()
            return redirect('/membership')
        except:
            pass

    context = {'member': member}
    return redirect('/membership', context)


def add_member(request):
    is_success = "fail"
    if request.method == 'POST':
        form = MemberForm(request.POST)
        print(form.errors)
        if form.is_valid():
            try:
                form.save()
                is_success = "success"
                return redirect('/membership', {'is_success': is_success})
            except:
                pass
    else:
        form = MemberForm()

    context = {
        'form': form,
        'is_success': is_success
    }
    return redirect('/membership', context)

