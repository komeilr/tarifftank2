from django.shortcuts import render
from django.http import JsonResponse, Http404
from utils.classes import TariffCA


def index(request):
    return render(request, 'index.html')

def search(request):
    query:str = request.GET.get('query')
    
    
    # HS code search
    if query.isdigit():
        try:
            t = TariffCA(query)
            return JsonResponse(t.gen_tariff_dict())

        except ValueError as e:
            raise Http404
            #return HttpResponseNotFound("Invalid HS Code. Please Try Again!")
    
    # Text Search    
    elif query.isalpha():
        return JsonResponse({"query": query})
    
    # multi text search
    elif all(x.isalpha() or x.isspace() for x in query):
        search_strings = query.split()
        return JsonResponse({"query": search_strings})
    
    
def hscodeNotFound(request, exception):
    return render(request, '404.html', status=404)
