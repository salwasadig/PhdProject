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

model = ML.MLmodel()
X_train, X_test, Y_train, Y_test, df = model.get_data()

def DT_model(data):
    if not os.path.exists('finalized_DT_model.sav'):
        # save the model to disk
        DT = model.DecisionTree()
        filename = 'finalized_DT_model.sav'
        pickle.dump(DT, open(filename, 'wb'))
    else:
        DT = pickle.load(open('finalized_DT_model.sav', 'rb'))
    predected = DT.predict(data)
    return predected[0]

def RF_model(data):    
    if not os.path.exists('finalized_RF_model.sav'):
        # save the model to disk
        RF = model.RandomForest()
        filename = 'finalized_RF_model.sav'
        pickle.dump(RF, open(filename, 'wb'))  
    else:
        RF = pickle.load(open('finalized_RF_model.sav', 'rb'))
    predected = RF.predict(data)
    return predected[0]


def home(request):
    return render(request, 'main/home.html')

def dashboard(request):
    return render(request, 'main/charts.html')

def charts(request):
    datadict = df['main_category'].value_counts().to_dict()
    #lunched = df['main_category'].groupby(df.launched.dt.year).count().to_dict()
    return HttpResponse(convert_dict_json(datadict))

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
            #post.author = request.user
            post.save()
            return redirect('/result/{}'.format(post.pk))
    else:
        form = FeaturesForm()
    return render(request, 'main/form.html', {'form': form})

def result(request, id):
    data = ProjectFeature.objects.get(id=id)
    y = pd.DataFrame([[data.main_category_id, data.backers, data.country_id, data.usd_goal_real,data.duration_days]])
    RF_predicted = RF_model(y)
    DT_predicted = DT_model(y)
    ProjectFeature.objects.filter(id=id).update(predected = DT_predicted)
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