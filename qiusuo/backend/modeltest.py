# coding=utf-8
from django.test import TestCase
from .models import Attention, User, Studio, Forbid

class modeltest(TestCase):
    def setup(self):
        userdic = {'username':'yc', 'password':'123456', 'telephone':'18711111111'}
        attiondic = {'username':'yc', 'teachername':'xbz'}
        Attention.objects.create(**attiondic)
        User.objects.create(**userdic)


    def testGet(self):
        userdic = {'username':'yc', 'password':'123456', 'telephone':'18711111111'}
        attiondic = {'username':'yc', 'teachername':'xbz'}
        result1 = Attention.objects.get(**attiondic)
        self.assertTrue(result1.status)

        result2 = User.objects.get(**userdic)
        self.assertTrue(result2.status)

    def testDelete(self):
        userdic = {'username':'yc', 'password':'123456', 'telephone':'18711111111'}
        attiondic = {'username':'yc', 'teachername':'xbz'}
        result = Attention.objects.delete(**attiondic)
        self.assertTrue(result.status)

        result1 = User.objects.delete(**userdic)
        self.assertTrue(result1.status)
