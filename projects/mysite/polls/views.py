from django.http import HttpResponse


def indexfunc(request):
    return HttpResponse("hey its great ,this is my first django app.")