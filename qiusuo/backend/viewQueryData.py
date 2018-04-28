from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from . import MyUtils
import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def querydata(request):
    username = request.POST['username']
    dic = {}
    dics = {
        'username':username,
    }
    try:
        tempObj = User.objects.filter(**dics).values('telephone','email','gender')
        if len(tempObj) == 0:
            dic['success'] = False
            dic['users'] = ": no query results."
        else:
            dic['success'] = True
            dic['users'] = MyUtils.parseToList(tempObj)
    except Exception:
        return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    return HttpResponse(simplejson.dumps(dic),content_type="application/json")
