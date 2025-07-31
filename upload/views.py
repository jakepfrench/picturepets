from django.http import HttpResponse

def upload(request):
    return HttpResponse("upload")

def gallery(request):
    return HttpResponse("gallery")