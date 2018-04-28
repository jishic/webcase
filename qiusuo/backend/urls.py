from django.conf.urls import include, url
from django.contrib import admin
from . import viewLogin
from . import viewRegist
from . import viewAttention
from . import viewSearch
from . import viewSendCode
from . import viewSendCodeFP
from . import viewACAttention
from . import viewACAttentionReturnList
from . import viewChangePassword
from . import viewForgetPassword
from . import viewQueryData
from . import viewChangeData
from . import viewLiveroomList
from . import viewLiveroomListIsStream
from . import viewStartStream
from . import viewFileUpload


urlpatterns = [
    url(r'^login$',viewLogin.login),
    url(r'^regist$',viewRegist.regist),
    url(r'^attention$',viewAttention.attention),
    url(r'^search$',viewSearch.search),
    url(r'^sendcode$',viewSendCode.sendcode),
    url(r'^sendcodefp$',viewSendCodeFP.sendcodefp),
    url(r'^acattention$',viewACAttention.acattention),
    url(r'^acattentionrl$',viewACAttentionReturnList.acattentionrl),
    url(r'^changepassword$',viewChangePassword.changepassword),
    url(r'^forgetpassword$',viewForgetPassword.forgetpassword),
    url(r'^querydata$',viewQueryData.querydata),
    url(r'^changedata$',viewChangeData.changedata),
    url(r'^liveroomlist$',viewLiveroomList.liveroomlist),
    url(r'^liveroomlistis$',viewLiveroomListIsStream.liveroomlistis),
    url(r'^startstream$',viewStartStream.startstream),
    url(r'^fileupload$',viewFileUpload.fileupload)
]
