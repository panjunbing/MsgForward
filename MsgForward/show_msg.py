# coding=utf-8

import json

from django.http import HttpResponse
from django.shortcuts import render


def show(request):
    try:
        # 将登录状态传递到session中
        user_id = request.POST.get('user_id')
        request.session['user_id'] = user_id
        request.session['is_login'] = True
        # 新建字典
        return_item = {'result': 'true'}
        # json转换
        result = json.dumps(return_item)
        return HttpResponse(result)
    except:
        return render(request, 'error.html')
