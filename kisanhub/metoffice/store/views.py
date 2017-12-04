from django.shortcuts import  render
from store.models import Weather
from graphos.sources.model import ModelDataSource
from graphos.renderers import flot
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def fn(request) :
    template=loader.get_template('store/graphs.html')
    queryset = Weather.objects.filter(attribute = 'Tmax', season = 'JAN')
    data_source = ModelDataSource(queryset, fields= ['region', 'value'])
    
    chart = flot.LineChart(data_source)
    context = {"chart": chart}
    return HttpResponse(template.render(context,request))


from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart

data =  [
        ['Year', 'Sales', 'Expenses'],
        [2004, 1000, 400],
        [2005, 1170, 460],
        [2006, 660, 1120],
        [2007, 1030, 540]
    ]