# coding=utf-8
from django.shortcuts import render
from msg_model import models


def login(request):
    return render(request, 'login.html')


def index(request):

    try:
        # 返回字段
        return_item = {}
        # 获取登录状态
        is_login = request.session.get('is_login')
        # 判断用户是否登录
        if is_login:
            # 获取该账号的msg
            user_id = request.session.get('user_id')
            user = models.User.objects.filter(id=user_id).first()
            role = user.role
            msg_list = models.Msg.objects.filter(role=role).order_by("-id")[0:5]

            # 获取msg信息
            list_msg = []
            for msg in msg_list:
                dict_msg = {'message': msg.message , 'create_time': msg.create_time.strftime("%Y-%m-%d %H:%M:%S")}
                list_msg.append(dict_msg)

            # 新建字典
            return_item = {'list_msg': list_msg, 'result': 'true'}
            return render(request, 'index.html', return_item)
        else:
            return_item = {'result': 'false'}
            return render(request, 'login_error.html', return_item)
    except Exception, e:
        return render(request, 'error.html')
