from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json


def main(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', context={})
    return HttpResponseRedirect(reverse('admin:login'))


def index(request):
    userjson = None

    if request.user:
        try:
            userjson = {
                'id': request.user.id,
                'email': request.user.email,
                'is_staff': request.user.is_staff,
                'is_superuser': request.user.is_superuser,
                'permissions': list(request.user.get_all_permissions())
            }
        except:
            pass

    userjson = json.dumps(userjson)

    # return render(request, 'index.html', context={'userjson': userjson})
    return render(request, 'index.html', context={})
