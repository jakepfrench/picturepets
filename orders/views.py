from django.http import HttpResponse

def order_list(request):
    return HttpResponse("order_list")

def new_order(request):
    return HttpResponse("new_order")