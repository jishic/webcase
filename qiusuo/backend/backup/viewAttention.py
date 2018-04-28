from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import Attention
from .models import Studio
from . import MyUtils
import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def attention(request):
    username = request.POST['username']
    try:
        obj = User.objects.filter(username=username).values('isTea')
        if obj[0]['isTea'] == False:
            attObj = Attention.objects.filter(username=username).values('teachername')#该用户关注的教师
            stuObj = Studio.objects.filter(isstream=True).values('teachername')#正在直播的教师
            teaidList = []
            for i in stuObj:
                teaidList.append(i['teachername'])
            resList = []
            for value1 in attObj:
                if value1['teachername'] in teaidList:
                    # resList.append({value1['teachername']:True})
                    tempDict = {}
                    tempDict['name'] = value1['teachername']
                    tempDict['type'] = True
                    resList.append(tempDict)
                else:
                    # resList.append({value1['teachername']:False})
                    tempDict = {}
                    tempDict['name'] = value1['teachername']
                    tempDict['type'] = False
                    resList.append(tempDict)
            returnDict = {
                'success':True,
                'list':resList
            }
            print(resList)
            return HttpResponse(simplejson.dumps(returnDict),content_type="application/json")
        else:
            attObj = Attention.objects.filter(teachername=username).values('username')
            # tempList = MyUtils.parseToList(attObj)
            tempList = []
            for i in attObj:
                tempList.append(i['username'])
            tempDict = {
                'studentResult':tempList
            }
            return HttpResponse(simplejson.dumps(tempDict),content_type="application/json")
    except Exception:
        return HttpResponse(simplejson.dumps({'success':False}),content_type="application/json")
