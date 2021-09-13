from os import sep
from django.http import request
import pandas as pd
import csv
from django.template import loader
from django.http import HttpResponseRedirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from .utils import handle_uploaded_file
from .forms import DropDownForm

def CSV_page(input_data):
    template = loader.get_template('data/index.html')
    return HttpResponse(template.render())


def data_CSV(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['data_set'])
        return HttpResponseRedirect('clean_data/')

def clean_data(request):
    with open('data_set.csv','r', newline='') as csv_reader:
        reader = csv.DictReader(csv_reader)
        my_column = []
        null_values = {}
        df_mean = []
        df_std = []
        df_range = []
        fieldnames = reader.fieldnames
        for idx in range(len(fieldnames)):
            my_column.append(fieldnames[idx])
    df = pd.read_csv('data_set.csv', header=0, usecols=my_column)
    for idx in range(len(fieldnames)):
        null_values[my_column[idx]] = round((df[my_column[idx]].iloc[:].isnull().sum() / df.shape[0]), 3)
    for i in range(len(my_column)):
            df_mean.append(round(df[my_column[i]].mean(), 2))
            df_std.append(df[my_column[i]].std())
            df_range.append(df[my_column[i]].max() - df[my_column[i]].min())
    zippedList = zip(my_column,df_mean,df_std,df_range)
    template = loader.get_template('data/results.html')
    return HttpResponse(template.render({'null_values': null_values,'list':zippedList}, request))