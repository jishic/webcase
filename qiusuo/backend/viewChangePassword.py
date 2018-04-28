from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from . import MyUtils
import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def changepassword(request):
    username = request.POST['username']
    password = request.POST['password']
    newpassword = request.POST['newpassword']
    # print(username)
    # print(password)
    # print(newpassword)
    dic = {}
    dics = {
        'username':username,
        'password':password
    }
    try:
        tempObj = User.objects.filter(**dics)
        if len(tempObj) == 0:
            dic['success'] = False
        else:
            User.objects.filter(**dics).update(password=newpassword)
            dic['success'] = True
    except Exception:
        return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    return HttpResponse(simplejson.dumps(dic),content_type="application/json")
    # return HttpResponse(simplejson.dumps({'success':True}),content_type="application/json")
