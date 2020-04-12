from django.shortcuts import render
from django.http import HttpResponse
from membership.models import Member
from .models import Transaction
from django.db.models import Q


# Create your views here.
def transactions(request):
    if request.method == 'GET':
        name_search = request.GET.get('fuzzy_name_search')
        ids = None
        if name_search is not None:
            lookup = (
                Q(fname__icontains=name_search) |
                Q(lname__icontains=name_search))

            members = Member.objects.filter(lookup)
            
            transactions = Transaction.objects.filter(Q(member__in=members))

            print(transactions)


        service = request.GET.get('service')
        # if query is not None:
        #     lookups = Q(fname__icontain))
        #     members = Member.objects.filter(lookups)
        #     context = {'members': members}
        #     return render(request, 'accounting/transactions.html', context)
        # else:
        #     render(request, 'accounting/transactions.html', context)
        print(name_search)
        context = {'members': ids}
        render(request, 'accounting/transactions.html', context)

    members = Member.objects.all()

    context = {'members': members}
    return render(request, 'accounting/transactions.html', context)
