from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from django.http import  HttpResponse
import json
import ML.MLModels as ML
import pickle
import pandas as pd
import os
from .forms import FeaturesForm
from .models import ProjectFeature
from django.shortcuts import redirect
from django.db.models import Sum


model = ML.MLmodel()
X_train, X_test, Y_train, Y_test, df = model.get_data()


def scusses_fail():
    dfstate_1 = pd.DataFrame(df[df.state == 1.0].groupby('main_category').state.count())
    dfstate_0 = pd.DataFrame(df[df.state == 0.0].groupby('main_category').state.count())
    dfstate_0.reset_index(level=0, inplace=True)
    dfstate_1.reset_index(level=0, inplace=True)
    dfstate_0.columns = ['Category', 'Fail']
    dfstate_1.columns = ['Category', 'Sucsses']
    df_state_1_0 = dfstate_0.merge(dfstate_1, on='Category')
    return df_state_1_0.to_dict()

def DT_model(data):
    if not os.path.exists('finalized_DT_model.sav'):
        model.DecisionTree()
        DT = pickle.load(open('finalized_DT_model.sav', 'rb'))
    else:
        DT = pickle.load(open('finalized_DT_model.sav', 'rb'))
    predected = DT.predict(data)
    return predected[0]

def RF_model(data):    
    if not os.path.exists('finalized_RF_model.sav'):
        model.RandomForest()
        RF = pickle.load(open('finalized_RF_model.sav', 'rb'))
    else:
        RF = pickle.load(open('finalized_RF_model.sav', 'rb'))
    predected = RF.predict(data)
    return predected[0]


def home(request):
    return render(request, 'main/home.html')

def dashboardcharts(request):
    countries_chart = df.country.value_counts().to_dict()
    categories_chart = df.main_category.value_counts().to_dict()
    categories_launched_chart = df.main_category.groupby(df.launched.dt.year).count().to_dict()
    categories_sucsses_fail = scusses_fail()
    categories_pledged = df.pledged.groupby(df.main_category).count().to_dict()
    datacharts = {'countries':countries_chart,
                  'categoies':categories_chart,
                  'cat_launched':categories_launched_chart,
                  'cat_states':categories_sucsses_fail,
                  'cat_pledged':categories_pledged}
    return HttpResponse(convert_dict_json(datacharts))

def projectscharts(request):
    allprojects = ProjectFeature.objects.count()
    DT_success = ProjectFeature.objects.filter(DT_predicted = 1).count()
    DT_fail = ProjectFeature.objects.filter(DT_predicted = 0).count()
    RF_success = ProjectFeature.objects.filter(RF_predicted = 1).count()
    RF_fail = ProjectFeature.objects.filter(RF_predicted = 0).count()
    if allprojects:
        successper = round((DT_success+RF_success)/(allprojects * 2) * 100, 2)
        failper = round((DT_fail+RF_fail)/(allprojects*2) * 100, 2)
        context = {'allprojects':allprojects, 'success': DT_success+RF_success,'successper':successper, 'fail': DT_fail+RF_fail, 'failper':failper}
    else:
        context = {'allprojects':'', 'success': '','successper':'', 'fail': '', 'failper':''}
    return render(request, 'main/projectscharts.html', context)
    

def convert_dict_json(dic):
    jsonData = []
    jsonData.append(json.dumps([{'label': item[0], 'value': item[1]} for item in dic.items()]))
    return jsonData

def predect(request):
    form = FeaturesForm()
    context = {'form': form}
    return render(request, 'main/form.html', context=context)

def savePredict(request):
    if request.method == "POST":
        form = FeaturesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/result/{}'.format(post.pk))
    else:
        form = FeaturesForm()
    return render(request, 'main/form.html', {'form': form})

def result(request, id):
    data = ProjectFeature.objects.get(id=id)
    y = pd.DataFrame([[data.main_category_id, data.country_id, data.usd_pledged, data.usd_goal_real,data.duration_days]])
    RF_predicted = RF_model(y)
    DT_predicted = DT_model(y)
    ProjectFeature.objects.filter(id=id).update(DT_predicted = DT_predicted, RF_predicted = RF_predicted)
    context={'data':data, 'DT':DT_predicted, 'RF':RF_predicted}
    return render(request, 'main/result.html', context=context)

def myprojects(request):
    projects = ProjectFeature.objects.all()
    context = {'projects':projects}
    return render(request, 'main/myprojects.html', context=context)

def getProject(request, id):
    project = ProjectFeature.objects.get(pk=id)
    form = FeaturesForm(instance=project)
    context={'form':form, 'project': project}
    return render(request, 'main/getProject.html', context=context)

def updatePredict(request, id):
    if request.method == "POST":
        project = ProjectFeature.objects.get(id=id)
        form = FeaturesForm(request.POST, instance= project)
        if form.is_valid():
            form.save()
            return redirect('/result/{}'.format(id))
    else:
        form = FeaturesForm()
    return render(request, 'main/form.html', {'form': form})