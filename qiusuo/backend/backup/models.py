from django.db import models

#让上传的文件路径动态地与user的名字有关
def upload_to(instance, filename):
    return '/'.join([MEDIA_ROOT, instance.username, filename])

class User(models.Model):
    """docstring for [object Object]."""
    username = models.CharField(max_length = 20, verbose_name = "用户名", primary_key = True)
    password = models.CharField(max_length = 42, verbose_name = "用户密码")
    telephone = models.CharField(max_length = 11, verbose_name = "用户电话")
    email = models.CharField(max_length = 20, verbose_name = "用户邮箱", default = "", blank = True, null = True)
    isTea = models.BooleanField(default = False)
    gender = models.BooleanField(default = False)
    imgpath = models.CharField(max_length = 160, verbose_name = "图片路径", default = "")

class Attention(models.Model):
    """docstring for [object Object]."""
    username = models.CharField(max_length = 20, verbose_name = "用户名")
    teachername = models.CharField(max_length = 20, verbose_name = "用户名")
    class Meta:
        """docstring for [object Object]."""
        unique_together = ('username','teachername')

class Studio(models.Model):
    """docstring for [object.Object]."""
    roomnum = models.CharField(max_length = 6, verbose_name = "直播间号", default = "", blank = False)
    roomtitle = models.CharField(max_length = 40, verbose_name = "直播间标题", default= "", blank = True, null = True)
    teachername = models.ForeignKey(User, on_delete = models.CASCADE)
    isstream =  models.BooleanField(default = False)

class Forbid(models.Model):
    """docstring for [object Object]."""
    teachername = models.CharField(max_length = 20, verbose_name = "用户名")
    banedname = models.CharField(max_length = 20, verbose_name = "被禁名")
    class Meta:
        """docstring for [object Object]."""
        unique_together = ('teachername','banedname')
