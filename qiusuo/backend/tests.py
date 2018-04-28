from django.test import TestCase
from django.test.client import Client
from .models import User
from . import MyUtils
import simplejson

class MyTest(TestCase):
    def testLogin(self):
        print('This is unit test of viewLogin: ')
        clientTemp = Client()
        dic = {'username':'lsh', 'password':'123456'}
        response = clientTemp.post("http://localhost:8000/backend/login",
        dic,
        content_type='application/json')
        print(response.content)

    def testRegist(self):
        print('This is unit test of viewRegist: ')
        clientTemp = Client()
        dic = {'username':'yc', 'password':'123456', 'telephone':'18711111111'}
        response = clientTemp.post("http://localhost:8000/backend/regist",
        simplejson.dumps(dic),
        content_type='application/json')
        print(response.content)

    def testAttention(self):
        print('This is unit test of viewAttention: ')
        clientTemp = Client()
        dic = {'username':'lsh'}
        response = clientTemp.post("http://localhost:8000/backend/attention",
        simplejson.dumps(dic),
        content_type='application/json')
        print(response.content)

    def testACAttention(self):
        print('This is unit test of viewACAttention: ')
        clientTemp = Client()
        dic = {'username':'yc', 'teachername':'xbz'}
        response = clientTemp.post("http://localhost:8000/backend/acattention",
        simplejson.dumps(dic),
        content_type='application/json')
        print(response.content)

    def testSearch(self):
        print('This is unit test of viewSearch: ')
        clientTemp = Client()
        dic = {'mysql':'xb'}
        response = clientTemp.post("http://localhost:8000/backend/search",
        simplejson.dumps(dic),
        content_type='application/json')
        print(response.content)

    def testSendCode(self):
        print('This is unit test of viewSendCode: ')
        clientTemp = Client()
        dic = {'telephone':'18756961985', 'verificationcode':'154869'}
        response = clientTemp.post("http://localhost:8000/backend/sendcode",
        simplejson.dumps(dic),
        content_type='application/json')
        print(response.content)

    def testLiveroomList(self):
        print('This is unit test of viewLiveroomList: ')
        clientTemp = Client()
        response = clientTemp.post("http://localhost:8000/backend/liveroomlist")
        print(response.content)

    # def testQueryData(self):
    #     print('This is unit test of viewQueryData: ')
    #     clientTemp = Client()
    #     dic = {'username':'lsh'}
    #     response = clientTemp.post("http://localhost:8000/backend/querydata",
    #     simplejson.dumps(dic),
    #     content_type='application/json')
    #     print(response.content)

    def testChangeData(self):
        print('This is unit test of viewChangeData: ')
        clientTemp = Client()
        dic = {'username':'xbx', 'telephone':'18799999999', 'email':'577777777@qq.com', 'gender':True}
        response = clientTemp.post("http://localhost:8000/backend/changedata",
        simplejson.dumps(dic),
        content_type='application/json')
        print(response.content)

    def testChangePassword(self):
        print('This is unit test of viewChangePassword: ')
        clientTemp = Client()
        dic = {'username':'lsh', 'password':'123456', 'newpassword':'12345'}
        response = clientTemp.post("http://localhost:8000/backend/changepassword",
        simplejson.dumps(dic),
        content_type='application/json')
        print(response.content)

    def testStartStream(self):
        print('This is unit test of viewStartStream: ')
        clientTemp = Client()
        dic = {'teachername':'xbx', 'isstream':True}
        response = clientTemp.post("http://localhost:8000/backend/startstream",
        simplejson.dumps(dic),
        content_type='application/json')
        print(response.content)
