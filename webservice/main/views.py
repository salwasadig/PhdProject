from django.shortcuts import render
from django.http import  HttpResponse
import json



def home(request):
    return render(request, 'main/home.html')

def dashboard(request):
    return render(request, 'main/charts.html')

def charts(reqest):
    datadict = df['main_category'].value_counts().to_dict()
    #lunched = df['main_category'].groupby(df.launched.dt.year).count().to_dict()
    return HttpResponse(convert_dict_json(datadict))

def convert_dict_json(dic):
    jsonData = []
    jsonData.append(json.dumps([{'label': item[0], 'value': item[1]} for item in dic.items()]))
    return jsonData