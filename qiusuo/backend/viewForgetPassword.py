from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from . import MyUtils
import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def forgetpassword(request):
    print('123')
    telephone = request.POST['telphone']
    newpassword = request.POST['newpass']
    dic = {}
    dics = {
        'telephone':telephone
    }
    # MyUtils.isNull(dics)
    dicts = {
    	'password':newpassword
    }
    try:
        tempObj = User.objects.filter(**dics)
        if len(tempObj) == 0:
            dic['success'] = False
        else:
            dic['success'] = True
            User.objects.filter(**dics).update(**dicts)
    except Exception:
        return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    return HttpResponse(simplejson.dumps(dic),content_type="application/json")
    # return HttpResponse(simplejson.dumps({'success':True}),content_type="application/json")
