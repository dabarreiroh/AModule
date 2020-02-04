from django.http import HttpResponse
from django.http import JsonResponse
from analizer_module.procesor.frame.url import URL
from analizer_module.procesor.risk.risk import Risk
from analizer_module.procesor.patterns.patterns import Patterns



def index(request):
    return HttpResponse("BAD REQUEST")

def query(request):
    urls= request.GET.get('url')
    publicid=request.GET.get('publicid','none public ID set')
    return JsonResponse({'url':urls,
                         "risk":Risk(list(filter(lambda x : x !="NaN",URL(urls.replace("'","")).path))).score(),
                         "paths": list(filter(lambda x : x !="NaN",URL(urls.replace("'","")).path)),
                         "coincidence":Risk(list(filter(lambda x : x !="NaN",URL(urls.replace("'","")).path))).coincidence(),
                         "public_id": publicid,
                         "assocpatterns":Patterns(list(filter(lambda x : x !="NaN",URL(urls.replace("'","")).path)),publicid).patterns()})



