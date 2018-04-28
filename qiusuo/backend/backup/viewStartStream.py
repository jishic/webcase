from django.shortcuts import render
from django.http import HttpResponse
from .models import Studio
from . import MyUtils
from django.db.models import Q
import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def startstream(request):
    teachername = request.POST['teachername']
    roomtitle = request.POST['roomtitle']
    roomnum = MyUtils.randomnum()
    # teachername = 'lqs'
    # roomtitle = '456'

    dicC = {
        'roomnum':'',
        'roomtitle':'',
        'isstream':False
    }
    dicO = {
        'roomnum':roomnum,
        'roomtitle':roomtitle,
        'isstream':True
    }
    dicOR = {
        'success':True,
        'roomnum':roomnum,
        'roomtitle':roomtitle
    }

    try:
        tempObj = Studio.objects.filter(teachername=teachername).values('roomnum', 'roomtitle', 'teachername', 'isstream')
        if len(tempObj):
            if tempObj[0]['isstream'] == True:
                Studio.objects.filter(teachername=teachername).update(**dicC)
                return HttpResponse(simplejson.dumps({'success':True, 'information':'close stream'}),content_type="application/json")
            else:
                Studio.objects.filter(teachername=teachername).update(**dicO)
                return HttpResponse(simplejson.dumps(dicOR),content_type="application/json")
        else:
            return HttpResponse(simplejson.dumps({'success':False, 'Error':'No teachername'}),content_type="application/json")
    except Exception:
        return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    # return HttpResponse(simplejson.dumps({'success':True}),content_type="application/json")
