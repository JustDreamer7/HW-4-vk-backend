from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from tenders.models import Tenders
from users.models import User


def index(request):
    name = request.POST.get('name')
    if name is None:
        name = 'Unknown'
    ctx = {'name': name}
    return render(request, 'index.html', ctx)


@require_GET
def get_tender_list(request):
    tenders = Tenders.objects.all()
    data = [
        {
            'id': tender.id,
            'title': tender.title,
            'law': tender.law,
            'price': tender.price
        } for tender in tenders
    ]
    return JsonResponse({'tenders': data})


@require_POST
def tender_create(request):
    title = request.POST.get('title')
    law = request.POST.get('law')
    price = request.POST.get('price')
    id = request.POST.get('id')
    email = User.objects.get(id=id).email
    Tenders.objects.create(title=title, law=law, price=price, user=User.objects.get(id=id))
    if None in (title, law, price):
        return HttpResponse(status=400)
    else:
        return JsonResponse({title: {'law': law, 'price': price, 'email': email}})


@require_POST
def tender_update(request):
    id = request.POST.get('id')
    upd_data = Tenders.objects.filter(id=id).update(title='test')
    return JsonResponse({'upd_data': upd_data})
# Переделать, чтобы апдейтить параметры можно только по выбору

@require_GET
def tender_detail_info(request):
    id = request.GET.get('id')
    detail_info = Tenders.objects.get(id=id)
    data = {
        'id': detail_info.id,
        'title': detail_info.title,
        'law': detail_info.law,
        'price': detail_info.price,
        'appication_deadline': detail_info.application_deadline,
        'user_id': detail_info.user_id
    }
    return JsonResponse({'detail_info': data})


@require_POST
def tender_delete(request):
    id = request.POST.get('id')
    Tenders.objects.filter(id=id).delete()
    return JsonResponse({'remove_data': id})
