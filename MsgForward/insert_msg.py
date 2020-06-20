from django.http import HttpResponse
from django.shortcuts import render
from msg_model.models import Msg


def insert(request):
    message = Msg(message=request.POST.get('msg'), role=request.POST.get('role'))
    return HttpResponse('true')
