from django.http import HttpResponse
from msg_model import models

def login(request):
    username = request.POST.get('username')
    passwd = request.POST.get('password')

    user = models.User.objects.filter(username=username).first()
    if user.username == username and user.passwd == passwd:
        result = 'true'
    else:
        result = 'false'
    return HttpResponse(result)
