from django.shortcuts import render
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.morris import LineChart, BarChart, DonutChart, AreaChart
from graphos.sources.simple import SimpleDataSource
from graphos.sources.model import ModelDataSource
from django.http import HttpResponse

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.db.models import Count, Sum, F
from django.db.models.functions import ExtractDay, ExtractWeek, ExtractMonth, ExtractYear

from django.views.generic.base import TemplateView, View
from stock.models import Product
from materials.models import Materials
from sales_order.models import SalesOrder
from purchase_order.models import PurchaseOrder
from invoice.models import Invoice

import json
from calendar import month_abbr, day_abbr, monthrange

LAST_WEEK = 1
LAST_MONTH = 2
LAST_YEAR = 3

YEAR_PAST = 10
def get_test(sample):
    data = [
        {'y': '2006', 'a': 100, 'b': 90 },
        {'y': '2007', 'a': 75, 'b': 65 },
        {'y': '2008', 'a': 50, 'b': 40 },
        {'y': '2009', 'a': 75, 'b': 65 },
        {'y': '2010', 'a': 50, 'b': 40 },
        {'y': '2011', 'a': 75, 'b': 65 },
        {'y': '2012', 'a': 100, 'b': 90 }
    ]

    return data

def get_weekly(object, range_, field, x_field):
    options = []
    data = []
    year = datetime.now().year

    str_year = year
    for i in range(1, 4):
        str_year = str(year) + " - " + str(year - (i*5))
        options.append(
            {
                'option': str_year,
                'index': i
            })

    sample = object.objects.filter(issued_date__range=[datetime(year=year-(int(range_)*5), month=12, day=31), datetime(year=year, month=12, day=31)])
    d = sample.values(x_field+'__year').annotate(Sum(field))
    
    for year_ in range(0, int(range_)*5):
        total_price_sum = 0.0
        for data_ in d:
            _year_ = data_[x_field+'__year']
            if year == _year_:
                total_price_sum = data_[field+'__sum']

        data.append({
            'y' : str(year),
            'a': total_price_sum,
            'b': 1,
        })
        year = year - 1

    return data, options

def get_monthly(object, month_selected, field, x_field):
    options = []
    data = []
    year = datetime.now().year
    months = list(month_abbr)
    _, days = monthrange(year, months.index(month_selected))

    for i in months[1:]:
        options.append({'option': i, 'index': i})

    sample = object.objects.filter(issued_date__year=year, issued_date__month=months.index(month_selected))
    d = sample.values(x_field+'__day').annotate(Sum(field))

    print("d : ", d)
    print("sample : ", sample)

    for monthly in range(1,days+1):
        total_price_sum = 0.0
        for data_ in d:
            month = data_[x_field+'__day']
            
            if monthly == month:
                total_price_sum = data_[field+'__sum']

        data.append({
            'y': monthly,
            'a': total_price_sum,
            'b': 1,
        })

    return data, options

def get_yearly(object, year_selected, field, x_field):
    options = []
    data = []
    year = datetime.now().year
    months = list(month_abbr)

    for i in range(0, YEAR_PAST):
        options.append({'option': year, 'index': year})
        year = year - 1

    sample = object.objects.filter(issued_date__year=year_selected)
    d = sample.values(x_field+'__month').annotate(Sum(field))

    
    for monthly in range(1,13):
        total_price_sum = 0.0
        for data_ in d:
            month = data_[x_field+'__month']
            
            if monthly == month:
                total_price_sum = data_[field+'__sum']
        data.append({
            'y' : months[monthly],
            'a': total_price_sum,
            'b': 1,
        })

    return data, options

def create_data_source(sample):
    data = [['Label', 'Quantity']]
    for _sample in sample.objects.all():
        data.append([
            _sample.name, _sample.quatity
        ])
    
    print('data : ', data)
    return data

def create_data_source_sm(sample):
    data = [['Label', 'Stock Margin', 'Quantity']]
    for _sample in sample.objects.all():
        data.append([
            _sample.name, _sample.stock_margin, _sample.quatity
        ])
    
    print('data : ', data)
    return data

class MorrisDemo(TemplateView):
    template_name = 'dashboard.html'
    renderer = None

    def get_context_data(self, **kwargs):
        context = super(MorrisDemo, self).get_context_data(**kwargs)
        context['segment'] = 'index' 

        # for stock card
        context['Stock_In'] = Product.objects.filter(status=0).count()
        context['Stock_Out'] = Product.objects.filter(status=1).count()
        stock_data_source = SimpleDataSource(data = [
            ['Label', 'Quantity'], 
            ['In Stock', context['Stock_In']],
            ['Out Stock', context['Stock_Out']]
        ])
        donut_chart_stock = DonutChart(stock_data_source, height=150, width=150)

        # for Materials card
        context['Materials_In'] = Materials.objects.filter(status=0).count()
        context['Materials_Out'] = Materials.objects.filter(status=1).count()
        material_data_source = SimpleDataSource(data = [
            ['Label', 'Quantity'], 
            ['In Stock', context['Materials_In']],
            ['Out Stock', context['Materials_Out']]
        ])
        donut_chart_material = DonutChart(material_data_source, height=150, width=150)

        # for Purchase card
        context['Purchase_Issued'] = PurchaseOrder.objects.filter(status=0).count()
        context['Purchase_Received'] = PurchaseOrder.objects.filter(status=2).count()
        purchase_data_source = SimpleDataSource(data = [
            ['Label', 'Quantity'], 
            ['Issued', context['Purchase_Issued']],
            ['Paid', PurchaseOrder.objects.filter(status=1).count()],
            ['Received', context['Purchase_Received']],
            ['Closed', PurchaseOrder.objects.filter(status=3).count()]
        ])
        donut_chart_purchase = DonutChart(purchase_data_source, height=150, width=150)


        # for Sales card
        context['Sales_Issued'] = SalesOrder.objects.filter(status=0).count()
        context['Sales_Produced'] = SalesOrder.objects.filter(status=1).count()
        sale_data_source = SimpleDataSource(data = [
            ['Label', 'Quantity'], 
            ['Issued', context['Sales_Issued']],
            ['Producing', context['Sales_Produced']],
            ['Sended', SalesOrder.objects.filter(status=2).count()],
            ['Returned', SalesOrder.objects.filter(status=3).count()], 
            ['Closed', SalesOrder.objects.filter(status=4).count()]
        ])
        donut_chart_sales = DonutChart(sale_data_source, height=150, width=150)

        context['donut_chart_1'] = donut_chart_stock
        context['donut_chart_2'] = donut_chart_material
        context['donut_chart_3'] = donut_chart_purchase
        context['donut_chart_4'] = donut_chart_sales

        # invoice graph
        # invoice_data = get_weekly(Invoice)
        Invoice_data = SimpleDataSource(get_test(Invoice))
        context['Invoice_chart'] = LineChart(Invoice_data, width=600, height=300)
        # print(get_weekly(Invoice), Invoice.objects.all())
        # print(Invoice_data)
        # queryset = Account.objects.all()
        # data_source = ModelDataSource(queryset,
        #                               fields=['year', 'sales'])

        data1 = [
            ['Label', 0],
            ['Out Stock', 1],
            ['In Stock', 2],
            ['Issued Stock', 2],
            ['Received Stock', 2]
        ]
        simple_data_source = SimpleDataSource(data=data1)
        line_chart = LineChart(simple_data_source)
        bar_chart = BarChart(simple_data_source)
        area_chart = AreaChart(simple_data_source)

        context['line_chart'] = line_chart 
        context['bar_chart'] = bar_chart
        context['area_chart'] = area_chart

        stock_overall_data_source = SimpleDataSource(data = create_data_source_sm(Product))
        materials_overall_data_source = SimpleDataSource(data = create_data_source_sm(Materials))

        context['chart_stock'] = BarChart(stock_overall_data_source, height=350, width=650)
        context['chart_materials'] = BarChart(materials_overall_data_source, height=350, width=650)
        # context = {
        #         "line_chart": line_chart,
        #        'bar_chart': bar_chart,
        #        'donut_chart_1': donut_chart_1,
        #        'donut_chart_2': donut_chart_2,
        #        'donut_chart_3': donut_chart_3,
        #        'donut_chart_4': donut_chart_4,
        #        'area_chart': area_chart,
        #        'segment': 'index' 
        #        }
        # context.update(super_context)
        return context



def invoice_dataset(request, index, value):

    data_set = []
    options = []

    if(index == LAST_WEEK):
        if(value != 'none'):
            data_set, options = get_weekly(Invoice, value, 'total_price', 'issued_date')
        else:
            data_set, options = get_weekly(Invoice, 5, 'total_price', 'issued_date')

    elif (index == LAST_MONTH):
        months = list(month_abbr)
        if(value!='none'):
            data_set, options = get_monthly(Invoice, value, 'total_price', 'issued_date')
        else:
            data_set, options = get_monthly(Invoice, months[datetime.now().month], 'total_price', 'issued_date')

    elif (index == LAST_YEAR):
        if(value!='none'):
            data_set, options = get_yearly(Invoice, value, 'total_price', 'issued_date')
        else:
            data_set, options = get_yearly(Invoice, datetime.now().year, 'total_price', 'issued_date')

    data = [
        {
            'data': data_set, 
            'options': options
        }
    ]
    
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


def stock_dataset(request, index, value):
    if(index == LAST_WEEK):
        if(value != 'none'):
            data_set, options = get_weekly(Product, value, 'total_price', 'issued_date')
        else:
            data_set, options = get_weekly(Product, 5, 'total_price', 'issued_date')

    elif (index == LAST_MONTH):
        months = list(month_abbr)
        if(value!='none'):
            data_set, options = get_monthly(Product, value, 'total_price', 'issued_date')
        else:
            data_set, options = get_monthly(Product, months[datetime.now().month], 'total_price', 'issued_date')

    elif (index == LAST_YEAR):
        if(value!='none'):
            data_set, options = get_yearly(Product, value, 'total_price', 'issued_date')
        else:
            data_set, options = get_yearly(Product, datetime.now().year, 'total_price', 'issued_date')

    data = [
        {
            'data': data_set, 
            'options': options
        }
    ]

    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')

def material_dataset(request, index):
    dataset = {}
    if(index == LAST_WEEK):
            data = [{
                'y': '2006',
                'a': 100,
                'b': 90
            },
            {
                'y': '2007',
                'a': 75,
                'b': 65
            },
            {
                'y': '2008',
                'a': 50,
                'b': 40
            },
            {
                'y': '2009',
                'a': 75,
                'b': 65
            },
            {
                'y': '2010',
                'a': 50,
                'b': 40
            },
            {
                'y': '2011',
                'a': 75,
                'b': 65
            },
            {
                'y': '2012',
                'a': 100,
                'b': 90
            }
        ]
    elif (index == LAST_MONTH):
            data = [{
                'y': '2006',
                'a': 100,
                'b': 90
            },
            {
                'y': '2007',
                'a': 75,
                'b': 65
            },
            {
                'y': '2008',
                'a': 50,
                'b': 40
            },
            {
                'y': '2009',
                'a': 75,
                'b': 65
            },
            {
                'y': '2010',
                'a': 50,
                'b': 40
            },
            {
                'y': '2011',
                'a': 75,
                'b': 65
            },
            {
                'y': '2012',
                'a': 100,
                'b': 90
            }
        ]
    elif (index == LAST_YEAR):
            data = [{
                'y': '2006',
                'a': 100,
                'b': 90
            },
            {
                'y': '2007',
                'a': 75,
                'b': 65
            },
            {
                'y': '2008',
                'a': 50,
                'b': 40
            },
            {
                'y': '2009',
                'a': 100,
                'b': 90
            },
            {
                'y': '2010',
                'a': 50,
                'b': 40
            },
            {
                'y': '2011',
                'a': 75,
                'b': 65
            },
            {
                'y': '2012',
                'a': 50,
                'b': 40
            }
        ]

    data = []
    data_set, options = get_yearly(Invoice, 2021)
    data = [
        {
            'data': data_set, 
            'options': options
        }
    ]

    dump = json.dumps(data)
    print("dump : ",dump)
    return HttpResponse(dump, content_type='application/json')

def purchase_dataset(request, index, value):
    if(index == LAST_WEEK):
        if(value != 'none'):
            data_set, options = get_weekly(PurchaseOrder, value, 'total_price', 'issued_date')
        else:
            data_set, options = get_weekly(PurchaseOrder, 5, 'total_price', 'issued_date')

    elif (index == LAST_MONTH):
        months = list(month_abbr)
        if(value!='none'):
            data_set, options = get_monthly(PurchaseOrder, value, 'total_price', 'issued_date')
        else:
            data_set, options = get_monthly(PurchaseOrder, months[datetime.now().month], 'total_price', 'issued_date')

    elif (index == LAST_YEAR):
        if(value!='none'):
            data_set, options = get_yearly(PurchaseOrder, value, 'total_price', 'issued_date')
        else:
            data_set, options = get_yearly(PurchaseOrder, datetime.now().year, 'total_price', 'issued_date')

    data = [
        {
            'data': data_set, 
            'options': options
        }
    ]
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')

def sales_dataset(request, index, value):
    if(index == LAST_WEEK):
        if(value != 'none'):
            data_set, options = get_weekly(SalesOrder, value, 'total_price', 'issued_date')
        else:
            data_set, options = get_weekly(SalesOrder, 5, 'total_price', 'issued_date')

    elif (index == LAST_MONTH):
        months = list(month_abbr)
        if(value!='none'):
            data_set, options = get_monthly(SalesOrder, value, 'total_price', 'issued_date')
        else:
            data_set, options = get_monthly(SalesOrder, months[datetime.now().month], 'total_price', 'issued_date')

    elif (index == LAST_YEAR):
        if(value!='none'):
            data_set, options = get_yearly(SalesOrder, value, 'total_price', 'issued_date')
        else:
            data_set, options = get_yearly(SalesOrder, datetime.now().year, 'total_price', 'issued_date')

    data = [
        {
            'data': data_set, 
            'options': options
        }
    ]

    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')

def overview_dataset(request, index):
    dataset = {}
    if(index == LAST_WEEK):
            data = [{
                'y': '2006',
                'a': 100,
                'b': 90
            },
            {
                'y': '2007',
                'a': 75,
                'b': 65
            },
            {
                'y': '2008',
                'a': 50,
                'b': 40
            },
            {
                'y': '2009',
                'a': 75,
                'b': 65
            },
            {
                'y': '2010',
                'a': 50,
                'b': 40
            },
            {
                'y': '2011',
                'a': 75,
                'b': 65
            },
            {
                'y': '2012',
                'a': 100,
                'b': 90
            }
        ]
    elif (index == LAST_MONTH):
            data = [{
                'y': '2006',
                'a': 100,
                'b': 90
            },
            {
                'y': '2007',
                'a': 75,
                'b': 65
            },
            {
                'y': '2008',
                'a': 50,
                'b': 40
            },
            {
                'y': '2009',
                'a': 75,
                'b': 65
            },
            {
                'y': '2010',
                'a': 50,
                'b': 40
            },
            {
                'y': '2011',
                'a': 75,
                'b': 65
            },
            {
                'y': '2012',
                'a': 100,
                'b': 90
            }
        ]
    elif (index == LAST_YEAR):
            data = [{
                'y': '2006',
                'a': 100,
                'b': 90
            },
            {
                'y': '2007',
                'a': 75,
                'b': 65
            },
            {
                'y': '2008',
                'a': 50,
                'b': 40
            },
            {
                'y': '2009',
                'a': 100,
                'b': 90
            },
            {
                'y': '2010',
                'a': 50,
                'b': 40
            },
            {
                'y': '2011',
                'a': 75,
                'b': 65
            },
            {
                'y': '2012',
                'a': 50,
                'b': 40
            }
        ]


    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')