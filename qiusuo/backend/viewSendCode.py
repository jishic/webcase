from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from . import MyUtils
import simplejson
from .smsclient import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sendcode(request):
    telephone = request.POST['telphone']
    verificationcode = request.POST['identify']
    # print(telephone)
    # print(verificationcode)
    dic = {}
    dics = {
    	'telephone':telephone
    }
    try:
    	tempObj = User.objects.filter(**dics)
    	if len(tempObj) != 0:
    		dic['success'] = False
    	else:
    		dic['success'] = True
    		smsClient = SmsClient()
    		smsClient.singleSend(telephone,verificationcode)
    except Exception:
    	return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    return HttpResponse(simplejson.dumps(dic),content_type="application/json")
    # return HttpResponse(simplejson.dumps({'success':True}),content_type="application/json")
