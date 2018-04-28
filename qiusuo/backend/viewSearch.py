from django.shortcuts import render
from django.http import HttpResponse
from .models import Studio
from . import MyUtils
from django.db.models import Q
import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def search(request):
    msql = request.POST['mysql']
    dicts = {}
    try:
        tempObj = Studio.objects.filter(Q(teacher__icontains=mysql)
        |Q(roomnum__icontains=mysql)
        |Q(roomtitle__icontains=mysql)).values('teachername','roomtitle','roomnum','isstream')
        if len(tempObj) ==0:
            dicts['success'] = False
            dicts['studios'] = ": no query results."
        else:
            dicts['success'] = True
            dicts['studios'] = MyUtils.parseToList(tempObj)
    except Exception:
        return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    return HttpResponse(simplejson.dumps(dicts),content_type="application/json")
    # dicts = {}
    # dicts['success'] = True
    # dicts['studios'] = {
    #     'roomnum':'100001',
    #     'roomtitle':'asdfg',
    #     'teachername':'xbz',
    #     'isstream':False
    # }
    # return HttpResponse(simplejson.dumps(dicts),content_type="application/json")
