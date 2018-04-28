from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import User
from . import MyUtils
from django.shortcuts import render_to_response
from PIL import Image
import simplejson
import os
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def fileupload(request):
    if request.method == "POST":
        img = request.FILES.get('image')
        username = request.POST['username']
        path = './frontend/static/'
        path1 = '/static/'
        dic = {
            'username':username
        }
        savepath = MyUtils.fileUploads(img, path, path1)
        try:
            dicImg = {
                'imgpath':savepath
            }
            tempObj = User.objects.filter(**dic)
            if len(tempObj) != 0:
                User.objects.filter(**dic).update(**dicImg)
                dicImg['success'] = True
                return HttpResponse(simplejson.dumps(dicImg),content_type="application/json")
            else:
                return HttpResponse(simplejson.dumps({'success':False,"information":"caozuoshibai"}),content_type="application/json")
        except Exception:
             return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    else:
        return HttpResponse(simplejson.dumps({'success':False,'information':'这不是合理的请求'}),content_type="application/json")
