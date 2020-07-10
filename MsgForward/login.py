# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from msg_model import models
from msg_model.models import Auth
import json


def login(request):
    # 新建字典
    return_item = {}
    try:
        # 获取账号
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.User.objects.filter(username=username).first()

        # 获取操作内容
        auth_msg = request.POST.get('auth_msg')
        create_time = timezone.now()
        # 判断登录
        if user is not None:
            auth = Auth(auth_msg=auth_msg, user_id=user.id, create_time=create_time)
            if user.username == username and user.passwd == password:
                request.session['user_id'] = user.id
                request.session['is_login'] = True
                return_item['result'] = 'true'
                auth.save()
            else:
                auth.auth_msg = 'login fail'
                auth.save()
                return_item['result'] = 'false'
                return_item['error'] = "用户名或密码错误"
        else:
            return_item['result'] = 'false'
            return_item['error'] = "用户名或密码错误"
        # json转换
        result = json.dumps(return_item)
        return HttpResponse(result)
    except Exception, e:
        return_item['result'] = 'false'
        return_item['error'] = e
        # json转换
        result = json.dumps(return_item)
        return HttpResponse(result)
