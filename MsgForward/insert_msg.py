from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from msg_model.models import Msg
from msg_model.models import Role

@csrf_exempt
def insert(request):
    try:
        key = request.POST.get('key')
        message = request.POST.get('msg')
        role_id = request.POST.get('role')
        role = Role.objects.filter(id=role_id).first()
        create_time = timezone.now()
        if key == "fFkfkU$2521Fk3&f223YhGHh":
            msg = Msg(message=message, role=role, create_time=create_time)
            msg.save()
        else:
            return HttpResponse("fail")
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse('insert successfully')
