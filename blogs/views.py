from django.http import HttpResponse


def home(request):
    return HttpResponse("This is our blogging platform index page")
