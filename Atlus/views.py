from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib import messages

from Atlus.forms import PredictForm
from Atlus.models import predicts
from Atlus.serializers import predictsSerializers

import pickle
import json
import numpy as np
import pandas as pd
import joblib



class PredictView(viewsets.ModelViewSet):
    queryset = predicts.objects.all()
    serializer_class = predictsSerializers

def predictform(request):
    if request.method == "POST":
        a = request.POST.get('info')
        a = a.splitlines()
        result = yesno(a)
        messages.success(request, result)
    return render(request, 'Atlus.html')
    
def yesno(a):
    try:
        mdl=joblib.load("content/assets/models/model.sav")
        mentalhealth_df = a
        numbersdf = [None] * 10

        male = set(["male", "m", "male-ish", "maile", "mal", "male (cis)", "make", "male ", "man", "msle", "mail", "malr", "cis man"])
        female = set(["cis female", "f", "female", "woman", "femake", "female ", "cis-female/femme", "female (cis)", "femail"])

        def yn(x,i):
            if x == "Yes":
                numbersdf[i] = 1
            else:
                numbersdf[i] = 0


        def ydkn(x,i):
            if x == "Yes":
                numbersdf[i] = 2
            elif x == "Don't know":
                numbersdf[i] = 1
            else:
                numbersdf[i] = 0


        def ymn(x,i):
            if x == "Yes":
                numbersdf[i] = 2
            elif x == "Maybe":
                numbersdf[i] = 1
            else:
                numbersdf[i] = 0


        def ysotn(x,i):
            if x == "Yes":
                numbersdf[i] = 2
            elif x == "Some of them":
                numbersdf[i] = 1
            else:
                numbersdf[i] = 0
                
        numbersdf[0] = int(mentalhealth_df[0])/100

        if mentalhealth_df[1].lower() in female:
            numbersdf[1] = 1
        else:
            numbersdf[1] = 0
            
        if mentalhealth_df[1].lower() in male:
            numbersdf[2] = 1
        else:
            numbersdf[2] = 0
            
        yn(mentalhealth_df[2],3)

        yn(mentalhealth_df[3],4)


        if mentalhealth_df[4] == "Often":
            numbersdf[5] = 3
        elif mentalhealth_df[4] == "Sometimes":
            numbersdf[5] = 2
        elif mentalhealth_df[4] == "Rarely":
            numbersdf[5] = 1
        else:
            numbersdf[5] = 0

        if mentalhealth_df[5] == "1-5":
            numbersdf[6] = 1
        elif mentalhealth_df[5] == "6-25":
            numbersdf[6] = 2
        elif mentalhealth_df[5] == "26-100":
            numbersdf[6] = 3
        elif mentalhealth_df[5] == "100-500":
            numbersdf[6] = 4
        elif mentalhealth_df[5] == "500-1000":
            numbersdf[6] = 5
        elif mentalhealth_df[5] == "More than 1000":
            numbersdf[6] = 6
        else:
            numbersdf[6] = 0

        yn(mentalhealth_df[6],7)
        yn(mentalhealth_df[7],8)
        ydkn(mentalhealth_df[8],9)

        numbersdf = list(map(float, numbersdf))
        numbersdf = (np.asarray(numbersdf)).reshape(1, -1)
        result = mdl.predict(numbersdf)
        if result == 0:
            return "You Probably do not require Medical Attention"
        else:
            return "You Should Probably Visit Psychologist Often"
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)