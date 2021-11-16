from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST, require_GET

from users.models import User


# Create your views here.
@require_GET
def get_user_list(request):
    users = User.objects.all()
    data = [
        {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'company': user.company
        } for user in users
    ]
    return JsonResponse({'users': data})


@require_POST
def user_create(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    company = request.POST.get('company')
    User.objects.create(username=username, email=email, company=company)
    if None in (username, email, company):
        return HttpResponse(status=400)
    else:
        return JsonResponse({username: {'email': email, 'company': company}})


@require_GET
def user_detail_info(request):
    id = request.GET.get('id')
    detail_info = User.objects.get(id=id)
    data = {
        'id': detail_info.id,
        'username': detail_info.username,
        'email': detail_info.email,
        'company': detail_info.company,
        'is_superuser': detail_info.is_superuser
    }
    return JsonResponse({'detail_info': data})


@require_POST
def user_update(request):
    id = request.POST.get('id')
    upd_data = User.objects.filter(id=id).update(title='test')
    return JsonResponse({'upd_data': upd_data})


@require_POST
def user_delete(request):
    id = request.POST.get('id')
    remove_data = User.objects.filter(id=id).delete()
    return JsonResponse({'remove_data': remove_data})
