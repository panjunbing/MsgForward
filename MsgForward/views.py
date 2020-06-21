# coding=utf-8
from django.shortcuts import render
from msg_model import models


def login(request):
    return render(request, 'login.html')


def index(request):
    # 获取该账号的msg
    user_id = request.session.get('user_id')
    user = models.User.objects.filter(id=user_id).first()
    role = user.role
    msg_list = models.Msg.objects.filter(role=role).order_by("-id")[0:5]

    # 获取msg信息
    list_msg = []
    for msg in msg_list:
        list_msg.append(msg.message)

    # 新建字典
    return_item = {'msg': list_msg, 'result': 'true'}

    return render(request, 'index.html', return_item)
