from django.shortcuts import render
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.morris import LineChart, BarChart, DonutChart, AreaChart
from graphos.sources.simple import SimpleDataSource
from graphos.sources.model import ModelDataSource
from django.http import HttpResponse

from datetime import datetime
from django.db.models import Count, Sum, F
from django.db.models.functions import ExtractDay, ExtractWeek, ExtractMonth, ExtractYear

from django.views.generic.base import TemplateView, View
from stock.models import Product
from materials.models import Materials
from sales_order.models import SalesOrder
from purchase_order.models import PurchaseOrder
from invoice.models import Invoice

import json
from calendar import month_abbr, day_abbr

LAST_WEEK = 1
LAST_MONTH = 2
LAST_YEAR = 3

YEAR_PAST = 10

def get_weekly(object, day_selected):
    options = []
    data = []
    month = datetime.now().weekday()
    months = list(day_abbr)

    for month_ in months:
        options.append({'option': str(month_)})

    data = [
        {'y': '2006', 'a': 100, 'b': 90 },
        {'y': '2007', 'a': 75, 'b': 65 },
        {'y': '2008', 'a': 50, 'b': 40 },
        {'y': '2009', 'a': 75, 'b': 65 },
        {'y': '2010', 'a': 50, 'b': 40 },
        {'y': '2011', 'a': 75, 'b': 65 },
        {'y': '2012', 'a': 100, 'b': 90 }
    ]
    return data, options

def get_monthly(object, month_selected):
    options = []
    data = []
    month = datetime.now().month
    months = list(month_abbr)[1:]

    for month_ in months:
        options.append({'option': str(month_)})

    data = [
        {'y': '2006', 'a': 100, 'b': 90 },
        {'y': '2007', 'a': 75, 'b': 65 },
        {'y': '2008', 'a': 50, 'b': 40 },
        {'y': '2009', 'a': 75, 'b': 65 },
        {'y': '2010', 'a': 50, 'b': 40 },
        {'y': '2011', 'a': 75, 'b': 65 },
        {'y': '2012', 'a': 100, 'b': 90 }
    ]

    return data, options

def get_yearly(object, year_selected):
    options = []
    data = []
    year = datetime.now().year

    for i in range(0, YEAR_PAST):
        options.append({'option': year})
        year = year - 1

    sample = object.objects.filter(issued_date__year=year_selected)
    d = sample.values('issued_date__month').annotate(Sum('total_price'))
    
    # print("options : ", options)

    data = [
        {'y': '2006', 'a': 100, 'b': 90 },
        {'y': '2007', 'a': 75, 'b': 65 },
        {'y': '2008', 'a': 50, 'b': 40 },
        {'y': '2009', 'a': 75, 'b': 65 },
        {'y': '2010', 'a': 50, 'b': 40 },
        {'y': '2011', 'a': 75, 'b': 65 },
        {'y': '2012', 'a': 100, 'b': 90 }
    ]
    
    return data, options

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
        Invoice_data = SimpleDataSource(get_weekly(Invoice, 1))
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
        print('data : ', simple_data_source)
        line_chart = LineChart(simple_data_source)
        bar_chart = BarChart(simple_data_source)
        area_chart = AreaChart(simple_data_source)

        context['line_chart'] = line_chart 
        context['bar_chart'] = bar_chart
        context['area_chart'] = area_chart

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



def invoice_dataset(request, index):

    data = []
    if(index == LAST_WEEK):
        data_set, options = get_weekly(Invoice, 1)
        data = [
            {
                'data': data_set, 
                'options': options
            }
        ]
    elif (index == LAST_MONTH):
        data_set, options = get_monthly(Invoice, 1)
        data = [
            {
                'data': data_set, 
                'options': options
            }
        ]

    elif (index == LAST_YEAR):
        data_set, options = get_yearly(Invoice, 2021)
        data = [
            {
                'data': data_set, 
                'options': options
            }
        ]

    dump = json.dumps(data)
    print("dump : ",dump)
    
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')


def stock_dataset(request, index):
    dataset = {}
    if(index == LAST_WEEK):
        data = [
            {'y': '2006', 'a': 100, 'b': 90 },
            {'y': '2007', 'a': 75, 'b': 65 },
            {'y': '2008', 'a': 22, 'b': 40 },
            {'y': '2009', 'a': 0, 'b': 65 },
            {'y': '2010', 'a': 1, 'b': 40 },
            {'y': '2011', 'a': 75, 'b': 65 },
            {'y': '2012', 'a': 65, 'b': 90 }
        ]
    elif (index == LAST_MONTH):
            data = [
                {'y': '2006', 'a': 100, 'b': 90 },
                {'y': '2007', 'a': 75, 'b': 65 },
                {'y': '2008', 'a': 50, 'b': 40 },
                {'y': '2009', 'a': 75, 'b': 65 },
                {'y': '2010', 'a': 50, 'b': 40 },
                {'y': '2011', 'a': 75, 'b': 65 },
                {'y': '2012', 'a': 100, 'b': 90 }
            ]
    elif (index == LAST_YEAR):
            data = [
                {'y': '2006', 'a': 100, 'b': 90 },
                {'y': '2007', 'a': 75, 'b': 65 },
                {'y': '2008', 'a': 50, 'b': 40 },
                {'y': '2009', 'a': 75, 'b': 65 },
                {'y': '2010', 'a': 50, 'b': 40 },
                {'y': '2011', 'a': 75, 'b': 65 },
                {'y': '2012', 'a': 100, 'b': 90 }
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

def purchase_dataset(request, index):
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

def sales_dataset(request, index):
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