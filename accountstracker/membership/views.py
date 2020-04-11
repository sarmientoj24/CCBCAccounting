from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
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


def add_member(request):
    is_success = "fail"
    if request.method == 'POST':
        form = MemberForm(request.POST)
        print(form.errors)
        if form.is_valid():
            try:
                form.fname = form.cleaned_data['fname']
                form.lname = form.cleaned_data['lname']
                form.sex = form.cleaned_data['sex']
                form.bdate = form.cleaned_data['bdate']
                form.contact = form.cleaned_data['contact']
                form.address = form.cleaned_data['address']
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


# class AddMember(View):
#     def post(self, request):
#         fname = request.POST.get('fname', None)
#         lname = request.POST.get('lname', None)
#         sex = request.POST.get('sex', None)
#         bdate = request.POST.get('bdate', None)
#         contact = request.POST.get('contact', None)
#         address = request.POST.get('address', None)

#         success = "Fail"
#         try:
#             Member.objects.create(
#                 fname=fname,
#                 lname=lname,
#                 sex=sex,
#                 bdate=bdate,
#                 contact=contact,
#                 address=address
#             )
#         except:
#             success = "Success"

#         context = {'add_success': success}

#         return redirect('/membership', context)
