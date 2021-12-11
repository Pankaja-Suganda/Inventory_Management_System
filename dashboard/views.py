from django.shortcuts import render
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.morris import LineChart, BarChart, DonutChart, AreaChart
from graphos.sources.simple import SimpleDataSource
from graphos.sources.model import ModelDataSource

from django.views.generic.base import TemplateView

class MorrisDemo(TemplateView):
    template_name = 'dashboard.html'
    renderer = None

    def get_context_data(self, **kwargs):
        super_context = super(MorrisDemo, self).get_context_data(**kwargs)
        # queryset = Account.objects.all()
        # data_source = ModelD ataSource(queryset,
        #                               fields=['year', 'sales'])
        data1 = [
            ['Year', 'Sales', 'Expenses', 'Items Sold', 'Net Profit'],
            ['2004', 1000, 400, 100, 600],
            ['2005', 1170, 460, 120, 710],
            ['2006', 660, 1120, 50, -460],
            ['2007', 1030, 540, 100, 490],
            ]
        simple_data_source = SimpleDataSource(data=data1)
        print('data : ', simple_data_source)
        line_chart = LineChart(simple_data_source)
        bar_chart = BarChart(simple_data_source)
        donut_chart_1 = DonutChart(simple_data_source, height=150, width=150, align="center", colors= ['yellow'])
        donut_chart_2 = DonutChart(simple_data_source, height=150, width=150, align="center")
        donut_chart_3 = DonutChart(simple_data_source, height=150, width=150, align="center")
        donut_chart_4 = DonutChart(simple_data_source, height=150, width=150, align="center")
        area_chart = AreaChart(simple_data_source)
        context = {
                "line_chart": line_chart,
               'bar_chart': bar_chart,
               'donut_chart_1': donut_chart_1,
               'donut_chart_2': donut_chart_2,
               'donut_chart_3': donut_chart_3,
               'donut_chart_4': donut_chart_4,
               'area_chart': area_chart,
               'segment': 'index' 
               }
        context.update(super_context)
        return context