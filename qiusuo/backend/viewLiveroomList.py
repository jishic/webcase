from django.shortcuts import render
from django.http import HttpResponse
from .models import Studio
from . import MyUtils
import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def liveroomlist(request):
    dicts ={}
    try:
        tempObj = Studio.objects.all().values('roomnum', 'roomtitle', 'teachername', 'isstream', 'stuimgpath')
        if len(tempObj) == 0:
            dicts['success'] = False
            dicts['information'] = ": no query results."
        else:
            dicts['success'] = True
            dicts['information'] = MyUtils.parseToList(tempObj)
    except Exception:
        return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    return HttpResponse(simplejson.dumps(dicts),content_type="application/json")
