from django.http.response import JsonResponse, HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from rest_framework import viewsets, status
from rest_framework.response import Response
from application.decorators import login_required, login_required_for_methods
from users.models import User
from users.serializers import UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @login_required_for_methods
    def list(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)

    @login_required_for_methods
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # @login_required_for_methods
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # @login_required_for_methods
    def perform_create(self, serializer):
        serializer.save()

    # @login_required_for_methods
    def update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # @login_required_for_methods
    def perform_update(self, serializer):
        serializer.save()

    @login_required_for_methods
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    @login_required_for_methods
    def perform_destroy(self, instance):
        instance.delete()


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')


@require_GET
@login_required
def get_user_list(request):
    users = User.objects.filter(email=request.user)
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
@login_required
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
@login_required
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
@login_required
def user_update(request):
    id = request.POST.get('id')
    username = request.POST.get('username')
    email = request.POST.get('email')
    company = request.POST.get('company ')
    updated_data = {}
    if username is not None:
        updated_data['username'] = username
    if email is not None:
        updated_data['email'] = email
    if company is not None:
        updated_data['company'] = company
    upd_data = User.objects.filter(id=id).update(**updated_data)
    return JsonResponse({'upd_data': upd_data})


@require_POST
@login_required
def user_delete(request):
    id = request.POST.get('id')
    remove_data = User.objects.filter(id=id).delete()
    return JsonResponse({'remove_data': remove_data})
