from django.shortcuts import render
from membership.models import Member
from .models import Transaction
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from datetime import datetime

PAGE_LIMIT = 20
THREE_O_CLOCK = 15

def transactions(request):
    if request.method == 'GET' and 'name' in request.GET:
        get_copy = request.GET.copy()
        parameters = get_copy.pop('page', True) and get_copy.urlencode()

        name_search = request.GET.get('name', None)
        service_search = request.GET.get('service', None)

        to_data = request.GET.get('to', '2030-01-01')
        from_data = request.GET.get('from', '2019-01-01')

        currency = request.GET.get('currency', 'PHP')

        to_data = '2030-01-01' if to_data is None or to_data == '' \
            else to_data

        from_data = '2019-01-01' if from_data is None or from_data == '' \
            else from_data

        transactions = Transaction.objects.filter(
            input_date__range=[from_data, to_data]
        )

        if service_search is not None and service_search != 'All':
            transactions = transactions.filter(
                service=service_search
            )

        if currency != 'ALL':
            transactions = transactions.filter(
                currency=currency
            )

        if name_search is not None:
            members = Member.objects.filter(
                Q(fname__icontains=name_search) |
                Q(lname__icontains=name_search)
            )

            transactions = transactions.filter(
                Q(member__in=members)
            )

        transactions = transactions.order_by("id")
        paginator = Paginator(transactions, PAGE_LIMIT)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1

        try:
            givings = paginator.page(page)
        except(EmptyPage, InvalidPage):
            givings = paginator.page(paginator.num_pages)

        parameters = {
            'name': name_search if name_search else '',
            'service': service_search if service_search else 'Worship',
            'to': to_data,
            'from': from_data,
            'currency': currency
        }

        context = {
            'givings': givings,
            'parameters': parameters
        }

    else:
        date_today = datetime.today().strftime('%Y-%m-%d')
        time_today = int(datetime.now().strftime('%H'))

        if time_today >= THREE_O_CLOCK:
            service_default = "Gospel"
        else:
            service_default = "Worship"

        currency_default = 'PHP'

        parameters = {
            'name': '',
            'service': service_default,
            'to': date_today,
            'from': date_today,
            'currency': currency_default
        }

        transactions = Transaction.objects.filter(
            input_date__range=[date_today, date_today]
        ).filter(
            currency=currency_default
        ).filter(
            service=service_default
        )

        transactions = transactions.order_by("id")
        paginator = Paginator(transactions, PAGE_LIMIT)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1

        try:
            givings = paginator.page(page)
        except(EmptyPage, InvalidPage):
            givings = paginator.page(paginator.num_pages)

        context = {
            'givings': givings,
            'parameters': parameters
        }

    paginated_total = {
        'tithe': sum([float(i.tithe) for i in givings]),
        'offering': sum([float(i.offering) for i in givings]),
        'firstfruit': sum([float(i.firstfruit) for i in givings]),
        'mission': sum([float(i.mission) for i in givings]),
        'care': sum([float(i.care) for i in givings]),
        'ladies': sum([float(i.ladies) for i in givings]),
        'men': sum([float(i.men) for i in givings]),
        'youth': sum([float(i.youth) for i in givings]),
        'choir': sum([float(i.choir) for i in givings]),
        'prayer_breakfast': sum([float(i.prayer_breakfast) for i in givings]),
        'circle_of_faith': sum([float(i.circle_of_faith) for i in givings]),
        'creative_team': sum([float(i.creative_team) for i in givings]),
        'dvbs': sum([float(i.dvbs) for i in givings]),
        'prison_ministry': sum([float(i.prison_ministry) for i in givings]),
        'others': sum([float(i.others) for i in givings]),
        'total': sum([float(i.total) for i in givings])
    }

    unpaginated_total = {
        'tithe': sum([float(i.tithe) for i in transactions]),
        'offering': sum([float(i.offering) for i in transactions]),
        'firstfruit': sum([float(i.firstfruit) for i in transactions]),
        'mission': sum([float(i.mission) for i in transactions]),
        'care': sum([float(i.care) for i in transactions]),
        'ladies': sum([float(i.ladies) for i in transactions]),
        'men': sum([float(i.men) for i in transactions]),
        'youth': sum([float(i.youth) for i in transactions]),
        'choir': sum([float(i.choir) for i in transactions]),
        'prayer_breakfast': sum([float(i.prayer_breakfast) for i in transactions]),
        'circle_of_faith': sum([float(i.circle_of_faith) for i in transactions]),
        'creative_team': sum([float(i.creative_team) for i in transactions]),
        'dvbs': sum([float(i.dvbs) for i in transactions]),
        'prison_ministry': sum([float(i.prison_ministry) for i in transactions]),
        'others': sum([float(i.others) for i in transactions]),
        'total': sum([float(i.total) for i in transactions])
    }

    context['paginated_total'] = paginated_total
    context['unpaginated_total'] = unpaginated_total

    return render(request, 'accounting/transactions.html', context)
