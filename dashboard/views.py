from django.shortcuts import render
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.morris import LineChart, BarChart, DonutChart, AreaChart
from graphos.sources.simple import SimpleDataSource
from graphos.sources.model import ModelDataSource

from django.views.generic.base import TemplateView
from stock.models import Product
from materials.models import Materials
from sales_order.models import SalesOrder
from purchase_order.models import PurchaseOrder

class MorrisDemo(TemplateView):
    template_name = 'dashboard.html'
    renderer = None

    def get_context_data(self, **kwargs):
        context = super(MorrisDemo, self).get_context_data(**kwargs)
        context['segment'] = 'index' 
        # for stock card
        context['Stock_In'] = Product.objects.filter(status=0).count()
        context['Stock_Out'] = Product.objects.filter(status=1).count()
        # for Materials card
        context['Materials_In'] = Materials.objects.filter(status=0).count()
        context['Materials_Out'] = Materials.objects.filter(status=1).count()
        # for Purchase card
        context['Purchase_Issued'] = SalesOrder.objects.filter(status=0).count()
        context['Purchase_Received'] = SalesOrder.objects.filter(status=2).count()
        # for Sales card
        context['Sales_Issued'] = PurchaseOrder.objects.filter(status=0).count()
        context['Sales_Produced'] = PurchaseOrder.objects.filter(status=1).count()
        # queryset = Account.objects.all()
        # data_source = ModelD ataSource(queryset,
        #                               fields=['year', 'sales'])


        data1 = [
            ['In Stock', 'Out Stock'],
            [2, 1],
            [2, 1]
            ]
        simple_data_source = SimpleDataSource(data=data1)
        print('data : ', simple_data_source)
        line_chart = LineChart(simple_data_source)
        bar_chart = BarChart(simple_data_source)
        donut_chart_1 = DonutChart(simple_data_source, height=200, width=200, align="center", colors= ['yellow'])
        donut_chart_2 = DonutChart(simple_data_source, height=150, width=150, align="center")
        donut_chart_3 = DonutChart(simple_data_source, height=150, width=150, align="center")
        donut_chart_4 = DonutChart(simple_data_source, height=150, width=150, align="center")
        area_chart = AreaChart(simple_data_source)
        context['line_chart'] = line_chart 
        context['bar_chart'] = bar_chart
        context['donut_chart_1'] = donut_chart_1
        context['donut_chart_2'] = donut_chart_2
        context['donut_chart_3'] = donut_chart_3
        context['donut_chart_4'] = donut_chart_4
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