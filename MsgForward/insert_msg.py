from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from msg_model.models import Msg


@csrf_exempt
def insert(request):
    try:
        message = request.POST.get('msg')
        role = request.POST.get('role')
        create_time = timezone.now()
        msg = Msg(message=message, role=role, create_time=create_time)
        msg.save()
    except:
        return render(request, 'error.html')
    return HttpResponse('true')
