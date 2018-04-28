from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import User
from django.shortcuts import render_to_response
from PIL import Image
import simplejson
import os
import random
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def fileupload(request):
    if request.method == "POST":
        img = request.FILES.get('image')
        img_file = Image.open(img)
        username = request.POST['username']
        dic = {
            'username':username
        }
        try:
            #保存图片
            path = './frontend/static/'
            filename = img.name
            filecode = str(random.randint(1000, 9999))
            img_file.thumbnail((200,200),Image.ANTIALIAS)
            img_file.save(path + filecode + filename)
            dicImg = {
                'imgpath':path + filecode + filename+""
            }
            tempObj = User.objects.filter(**dic)
            if len(tempObj) != 0:
                User.objects.filter(**dic).update(**dicImg)
                return HttpResponse(simplejson.dumps({'success':True}),content_type="application/json")
            else:
                return HttpResponse(simplejson.dumps({'success':False,"information":"caozuoshibai"}),content_type="application/json")
        except Exception:
             return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
    else:
        return HttpResponse(simplejson.dumps({'success':False,'information':'这不是合理的请求'}),content_type="application/json")
