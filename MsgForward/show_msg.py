from django.shortcuts import render


def show(request):
    name = request.POST.get('username')
    passwd = request.POST.get('password')
    return render(request, 'index.html')
