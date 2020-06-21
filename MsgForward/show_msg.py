# coding=utf-8
import string

from django.http import HttpResponse
from django.shortcuts import render, redirect

from msg_model import models
import json


def show(request):

    # 将登录状态传递到session中
    user_id = request.POST.get('user_id')
    request.session['user_id'] = user_id
    request.session['is_login'] = True

    # 新建字典
    return_item = {}






    return_item['result'] = 'true'
    # json转换
    result = json.dumps(return_item)
    return HttpResponse(result)
