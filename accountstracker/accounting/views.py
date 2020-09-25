from django.shortcuts import render
from membership.models import Member
from .models import Transaction
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from datetime import datetime
from io import StringIO
from django.http import HttpResponse
from xlsxwriter.workbook import Workbook
from django.shortcuts import redirect

PAGE_LIMIT = 4
THREE_O_CLOCK = 15

def transactions(request):
    if request.method == 'GET' and 'name' in request.GET:
        get_copy = request.GET.copy()
        uri_parameters = get_copy.pop('page', True) and get_copy.urlencode()

        name_search = request.GET.get('name', None)
        service_search = request.GET.get('service', None)

        to_data = request.GET.get('to', '2050-01-01')
        from_data = request.GET.get('from', '2019-01-01')

        currency = request.GET.get('currency', 'PHP')

        to_data = '2050-01-01' if to_data is None or to_data == '' \
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

        parameters = {
            'name': name_search if name_search else '',
            'service': service_search if service_search else 'Worship',
            'to': to_data,
            'from': from_data,
            'currency': currency
        }

        context = {
            'uri_parameters': uri_parameters,
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

        context = {
            'parameters': parameters
        }

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

    context['givings'] = givings
    context['paginated_total'] = paginated_total
    context['unpaginated_total'] = unpaginated_total

    return render(request, 'accounting/transactions.html', context)


from accounting.definitions import *

def export_to_csv(request):
    if request.method == 'GET':
        get_copy = request.GET.copy()
        uri_parameters = get_copy.pop('page', True) and get_copy.urlencode()

        name_search = request.GET.get('name', None)
        service_search = request.GET.get('service', None)

        date_today = datetime.today().strftime('%Y-%m-%d')

        to_data = request.GET.get('to', date_today)
        from_data = request.GET.get('from', date_today)

        currency = request.GET.get('currency', 'PHP')

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

        if transactions.exists():
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = "attachment; filename=test.xlsx"

            book = Workbook(response, {'in_memory': True})
            sheet = book.add_worksheet('Transaction')
            bold_cell_format = book.add_format({'bold': True}) 

            row = 0
            col = 0

            # Insert header
            for col_index, col_name in enumerate(output_cols_header):
                sheet.write(row, col_index, col_name, bold_cell_format)
            row += 1
            
            # Insert data
            for transaction in transactions:
                worksheet_array_data = get_row_data_to_worskheet_array(transaction)

                for col_index, trans_data in enumerate(worksheet_array_data):
                    sheet.write(row, col_index, trans_data)
                row += 1

            # Insert footer
            row += 1
            for column_header, column_marker in output_col_marker.items():
                cell_location = column_marker + str(row)
                if column_header == 'TRANS_ID':
                    sheet.write(cell_location, "TOTAL", bold_cell_format)

                else:
                    formula = '=SUM({}2:{}{})'.format(column_marker, column_marker, (row - 1))
                    sheet.write_formula(cell_location, formula)
            book.close()
            return response
    return redirect('transactions')


def get_row_data_to_worskheet_array(transaction):
    id = transaction.id
    last_name = transaction.member.lname
    first_name = transaction.member.fname
    trans_date = transaction.input_date
    service = transaction.service
    tithe = transaction.tithe
    offering = transaction.offering
    firstfruit = transaction.firstfruit
    firstfruit_year = transaction.firstfruit_year
    mission = transaction.mission
    care = transaction.care
    ladies = transaction.ladies
    men = transaction.men
    youth = transaction.youth
    choir = transaction.choir
    prayer = transaction.prayer_breakfast
    circle = transaction.circle_of_faith
    creative = transaction.creative_team
    dvbs = transaction.dvbs
    prison = transaction.prison_ministry
    other = transaction.others
    desc = transaction.others_description
    total = transaction.total

    data = [
        id, trans_date, firstfruit_year, service, last_name, first_name,
        tithe, offering, firstfruit, mission, care, ladies, men, youth,
        choir, prayer, circle, creative, dvbs, prison, other,
        desc, total
    ]

    return data

# worksheet.write_formula(2, 0, '=SUM(B1:B5)')


# # create the HttpResponse object ...
#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = "attachment; filename=test.xlsx"

#     # .. and pass it into the XLSXWriter
#     book = Workbook(response, {'in_memory': True})
#     sheet = book.add_worksheet('test')       
#     sheet.write(0, 0, 'Hello, world!')
#     book.close()

# def your_view(request):
#     # your view logic here

#     # create a workbook in memory
#     output = StringIO.StringIO()

#     book = Workbook(output)
#     sheet = book.add_worksheet('test')       
#     sheet.write(0, 0, 'Hello, world!')
#     book.close()

#     # construct response
#     output.seek(0)
#     response = HttpResponse(output.read(), mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
#     response['Content-Disposition'] = "attachment; filename=test.xlsx"

#     return response

