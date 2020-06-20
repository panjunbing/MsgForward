# coding=utf-8
import string

from django.http import HttpResponse
from django.shortcuts import render

from msg_model import models
import json


def show(request):
    # 获取该账号的msg
    user_id = request.POST.get('user_id')
    user = models.User.objects.filter(id=user_id).first()
    role = user.role
    msg_list = models.Msg.objects.filter(role=role).order_by("-id")[0:5]

    # 新建字典
    return_item = {}

    # 获取msg信息
    list = []
    for msg in msg_list:
        list.append(msg.message)

    return_item['msg'] = list
    print return_item
    return_item['result'] = 'true'
    return render(request, 'index.html')
