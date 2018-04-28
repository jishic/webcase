from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from . import MyUtils
import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    # print(username)
    # print(password)
    dics = {
        'username':username,
        'password':password
    }
    dic = {}
    try:
        tempObj = User.objects.filter(**dics).values('username','password'
        ,'telephone','email','isTea','gender','imgpath')
        print(len(tempObj))
        if len(tempObj) == 0:
            dic['success'] = False
        else:
            #dic['success'] = True
            dic = MyUtils.parseTodic(tempObj)
            dic['success'] = True
    except Exception:
        return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    return HttpResponse(simplejson.dumps(dic),content_type="application/json")
    # return HttpResponse(simplejson.dumps({'success':True}),content_type="application/json")
