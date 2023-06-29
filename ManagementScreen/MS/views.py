from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Max, F
from django.contrib import messages
from django.conf import settings
import json
from pathlib import Path
# Create your views here.

# management 

def management(request):
    managementjson =  settings.MEDIA_ROOT + '/' + 'management.json'
    try:
        with open(managementjson) as f:
            data = json.load(f)
    except:
        data ={}

    # print(data)
    jsonData = json.dumps(data)
    # print(jsonData)
    context = {
        'jsonData': jsonData
    }
    context.update(data)
    return render(request, 'ms/management.html', context)
