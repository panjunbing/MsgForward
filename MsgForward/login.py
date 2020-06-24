# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render

from msg_model import models
import json


def login(request):
    try:
        # 获取账号
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 新建字典
        return_item = {}
        # 判断登录
        user = models.User.objects.filter(username=username).first()
        if user is not None:
            if user.username == username and user.passwd == password:
                request.session['user_id'] = user.id
                request.session['is_login'] = True
                return_item['result'] = 'true'
            else:
                return_item['result'] = 'false'
        else:
            return_item['result'] = 'false'
        # json转换
        result = json.dumps(return_item)
        return HttpResponse(result)
    except Exception, e:
        return render(request, 'error.html')