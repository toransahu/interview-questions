from django.shortcuts import  render
from store.models import Weather, Climate
from graphos.sources.model import ModelDataSource
from graphos.renderers import flot
from django.template import loader
from django.http import HttpResponse

# Create your views here

def fn(request):
    from graphos.sources.simple import SimpleDataSource
    from graphos.renderers.gchart import LineChart, BarChart, ColumnChart
    # test data
    data =  [
            ['Year', 'Sales', 'Expenses'],
            [2004, 1000, 400],
            [2005, 1170, 460],
            [2006, 660, 1120],
            [2007, 1030, 540]
        ]
    
    data_source = SimpleDataSource(data=data)
    
    # Original DataSource object
    queryset = Weather.objects.filter(region = 'UK')
    queryset = Climate.objects.filter(region = 'UK',  year__gt=1000, year__lt=9999)
    data_source = ModelDataSource(queryset, fields= ['year','tmax', 'tmin'])
    data_source = ModelDataSource(queryset, fields= ['year', 'sunshine', 'rainfall'])
    
    # Chart object
    # chart = LineChart(data_source)
    # chart = BarChart(data_source)
    chart = ColumnChart(data_source)
    
    
    context = {'chart': chart}
    template=loader.get_template('store/fn2.html')
    
    return HttpResponse(template.render(context,request))
    