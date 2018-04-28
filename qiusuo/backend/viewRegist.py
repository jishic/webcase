from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from . import MyUtils
import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def regist(request):
    username = request.POST['username']
    password = request.POST['password']
    telephone = request.POST['telphone']
    # username = 'yc'
    # password = '123456'
    # telephone = '18456017581'
    dic = {
        'username':username,
        'password':password,
        'telephone':telephone
    }
    try:
        userObj = User.objects.create(**dic)
        userObj.save()
    except Exception:
        return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")

    return HttpResponse(simplejson.dumps({'success':True}),content_type="application/json")
