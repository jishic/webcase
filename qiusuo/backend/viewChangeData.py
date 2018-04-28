from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from . import MyUtils
import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def changedata(request):
    username = request.POST['username']
    telephone = request.POST['telephone']
    email = request.POST['email']
    intgender = request.POST['gender']
    if intgender == "1":
        # print("1")
        gender = True
    elif intgender == "0":
        gender = False
    dic = {}
    dics = {
        'username':username,
    }
    newdics = {
        'telephone':telephone,
        'email':email+"",
        'gender':gender
    }
    # if MyUtils.isNull(dics):
    #     return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    try:
        tempObj = User.objects.filter(**dics)
        if len(tempObj) == 0:
            dic['success'] = False
        else:
            User.objects.filter(**dics).update(**newdics)
            dic['success'] = True
    except Exception:
        return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    return HttpResponse(simplejson.dumps(dic),content_type="application/json")
    # return HttpResponse(simplejson.dumps({'success':True}),content_type="application/json")
