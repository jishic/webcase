from django.shortcuts import render
from django.http import HttpResponse
from .models import Studio
from .models import User
from . import MyUtils
from django.db.models import Q
import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def startstream(request):
    teachername = request.POST['username']
    roomtitle = request.POST['roomName']
    roomnum = MyUtils.randomnum()
    dicC = {
        'roomnum':'',
        'roomtitle':'',
        'isstream':False
    }
    dicO = {
        'roomnum':roomnum,
        'roomtitle':roomtitle,
        'isstream':True
    }

    try:
        tempObj = Studio.objects.filter(teachername=teachername).values('isstream')
        print(len(tempObj))
        if len(tempObj):
            if tempObj[0]['isstream'] == True:
                Studio.objects.filter(teachername=teachername).update(**dicC)
                return HttpResponse(simplejson.dumps({'success':True, 'information':'close stream'}),content_type="application/json")
            else:
                img = request.FILES.get('image')
                path = './frontend/static/'
                path1 = '/static/'
                savepath = MyUtils.fileUploads(img,path,path1)
                print(savepath)
                dicO['stuimgpath'] = savepath
                Studio.objects.filter(teachername=teachername).update(**dicO)
                imgObj = User.objects.filter(username=teachername).values('imgpath')
                dicO['imgpath'] = imgObj[0]['imgpath']
                dicO['success'] = True
                return HttpResponse(simplejson.dumps(dicO),content_type="application/json")
        else:
            img = request.FILES.get('image')
            path = './backend/image/'
            path1 = '/static/'
            savepath = MyUtils.fileUploads(img,path,path1)
            dicO['stuimgpath'] = savepath
            dicO['teachername'] = teachername
            userObj = Studio.objects.create(**dicO)
            userObj.save()
            imgObj = User.objects.filter(username=teachername).values('imgpath')
            dicO['imgpath'] = imgObj[0]['imgpath']
            dicO['success'] = True
            return HttpResponse(simplejson.dumps(dicO),content_type="application/json")
    except Exception:
        return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
