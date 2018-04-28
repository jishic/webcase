import simplejson
from .models import User
import random
from PIL import Image

def parseToList(tupleTemp):
    tempList = []
    for values in tupleTemp:
        dic = dict()
        for key,value in values.items():
            dic[key] = value
        tempList.append(dic)
    return tempList

def parseTodic(tupleTemp):
    dic = {}
    for key,value in tupleTemp[0].items():
        dic[key] = value
    return dic


def isEmptyQuery(tupleTemp):
    if len(tupleTemp) == 0:
        return True
    else:
        return False

def randomnum():
    number = str(random.randint(100, 1000))
    return number

def isNull(dicts):
    for key,value in dicts:
        if value == null:
            return True
    return False

def fileUploads(imgFile,imgpath,tempath):
    img_file = Image.open(imgFile)
    #保存图片
    filename = imgFile.name
    filecode = str(random.randint(1000, 9999))
    img_file.thumbnail((200,200),Image.ANTIALIAS)
    img_file.save(imgpath + filecode + filename)
    return tempath + filecode + filename + ""
