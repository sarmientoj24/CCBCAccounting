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

