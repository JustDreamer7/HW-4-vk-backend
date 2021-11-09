from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from random import randint, choice


def index(request):
    name = request.GET.get('name')
    if name is None:
        name = 'Unknown'
    ctx = {'name': name}
    return render(request, 'index.html', ctx)


def tender_detail(request):
    if request.method != 'GET':
        return HttpResponse(status=405)
    company = request.GET.get('company')
    if company is None:
        return JsonResponse({'Company': 'None'})
    return JsonResponse({company: {'law': choice(['44-FZ', '223-FZ', '94-FZ']), 'price': randint(int(1e5), int(1e9))}})


def tender_create(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    company = request.GET.get('company')
    law = request.GET.get('law')
    price = request.GET.get('price')
    if None in (company, law, price):
        return HttpResponse(status=400)
    else:
        return JsonResponse({company: {'law': law, 'price': price}})


def tender_list(request):
    if request.method != 'GET':
        return HttpResponse(status=405)
    return JsonResponse({'PIK': {'law': '44-FZ', 'price': 1242525}, 'MOSAGRO': {'law': '223-FZ', 'price': 424523}})
