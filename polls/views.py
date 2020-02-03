from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hola")

def query(request,urls,public_id):
    return JsonResponse({'url':urls,'id':public_id,"risk":"","coincidence":"","patterns":""})

