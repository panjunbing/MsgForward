# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from msg_model import models
from msg_model.models import Auth
import json


def login(request):
    try:
        # 新建字典
        return_item = {}

        # 获取账号
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.User.objects.filter(username=username).first()

        # 获取操作内容
        auth_msg = request.POST.get('auth_msg')
        create_time = timezone.now()
        auth = Auth(auth_msg=auth_msg, user_id=user.id, create_time=create_time)

        # 判断登录
        if user is not None:
            if user.username == username and user.passwd == password:
                request.session['user_id'] = user.id
                request.session['is_login'] = True
                return_item['result'] = 'true'
                auth.save()
            else:
                auth.auth_msg = 'login fail'
                auth.save()
                return_item['result'] = 'false'
        else:
            return_item['result'] = 'false'
        # json转换
        result = json.dumps(return_item)
        return HttpResponse(result)
    except Exception, e:
        return render(request, 'error.html')
