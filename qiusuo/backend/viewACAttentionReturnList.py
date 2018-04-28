from django.shortcuts import render
from django.http import HttpResponse
from .models import Attention
from . import MyUtils
import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def acattentionrl(request):
    username = request.POST['username']
    teachername = request.POST['teachername']
    # username = 'dingz'
    # teachername = 'xbz'
    dic = {}
    dics = {
        'username':username,
        'teachername':teachername
    }
    try:
        tempObj = Attention.objects.filter(**dics).values('username','teachername')
        print(len(tempObj))
        if len(tempObj) == 0:
            dic['success'] = False
            dic['information'] = 'Operating Error'
            return HttpResponse(simplejson.dumps(dic),content_type="application/json")
        else:
            Attention.objects.filter(**dics).delete()
            attObj = Attention.objects.filter(username = username).values('teachername')
            dic['success'] = True
            dic['attentionList'] = MyUtils.parseToList(attObj)
            return HttpResponse(simplejson.dumps(dic),content_type="application/json")
    except Exception:
        return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    # return HttpResponse(simplejson.dumps({'success':True}),content_type="application/json")
