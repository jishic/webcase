import simplejson
from .models import User
import random

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