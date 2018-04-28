from django.shortcuts import render
from django.http import HttpResponse
from .models import Attention
from . import MyUtils
import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def acattention(request):
    username = request.POST['username']
    teachername = request.POST['teachername']
    dic = {}
    dics = {
        'username':username,
        'teachername':teachername
    }
    try:
        tempObj = Attention.objects.filter(**dics).values('username','teachername')
        if len(tempObj) == 0:
            addObj = Attention.objects.create(**dics)
            addObj.save()
            return HttpResponse(simplejson.dumps({'success':True}),content_type="application/json")
        else:
            tempObj.delete()
            return HttpResponse(simplejson.dumps({'success':True}),content_type="application/json")
    except Exception:
        return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    # return HttpResponse(simplejson.dumps({'success':True}),content_type="application/json")
