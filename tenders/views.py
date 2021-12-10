from django.http.response import JsonResponse, HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from elasticsearch import Elasticsearch, RequestsHttpConnection
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_elasticsearch import es_views, es_filters, es_pagination

from application.decorators import login_required, login_required_for_methods
from tenders.documents import TendersDocument
from tenders.models import Tenders
from tenders.serializers import TenderSerializer, ElasticTenderSerializer
from users.models import User

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)

class TenderViewSet(viewsets.ModelViewSet):
    serializer_class = TenderSerializer
    queryset = Tenders.objects.all()

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


class TenderView(DocumentViewSet):
    document = TendersDocument
    serializer_class = ElasticTenderSerializer
    fielddata = True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
    search_fields = (
        'username',
        'email'
        'company',
    )
    multi_match_search_fields = (
        'title',
        'email'
        'content',
    )
    filter_fields = {
        'username': 'username',
        'company': 'company',
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ('id',)
    # es_client = Elasticsearch(hosts=['localhost:9200/'],
    #                           connection_class=RequestsHttpConnection)
    # es_model = TendersDocument
    # es_pagination_class = es_pagination.ElasticLimitOffsetPagination
    # es_filter_backends = (
    #     es_filters.ElasticFieldsFilter,
    #     es_filters.ElasticFieldsRangeFilter,
    #     es_filters.ElasticSearchFilter,
    #     es_filters.ElasticOrderingFilter,
    #     es_filters.ElasticGeoBoundingBoxFilter
    # )
    # # es_ordering = 'application_deadline'
    # es_filter_fields = (
    #     es_filters.ESFieldFilter('law', 'laws'),
    # )
    # es_range_filter_fields = (es_filters.ESFieldFilter('price'),)
    # es_search_fields = (
    #     'law',
    #     'title',
    # )

    # @classmethod
    # def get_extra_actions(cls):
    #     return []


@login_required
def index(request):
    name = request.POST.get('name')
    if name is None:
        name = 'Unknown'
    ctx = {'name': name}
    return render(request, 'index.html', ctx)


@require_GET
@login_required
def tender_list(request):
    tenders = Tenders.objects.filter(user=User.objects.get(email=request.user))
    print(User.objects.filter(email=request.user).first())
    data = [
        {
            'id': tender.id,
            'title': tender.title,
            'law': tender.law,
            'price': tender.price,
        } for tender in tenders
    ]
    return JsonResponse({'tenders': data})


@require_POST
@login_required
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


@login_required
@require_POST
def tender_update(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    law = request.POST.get('law')
    price = request.POST.get('price')
    updated_data = {}
    if title is not None:
        updated_data['title'] = title
    if law is not None:
        updated_data['law'] = law
    if price is not None:
        updated_data['price'] = price
    upd_data = Tenders.objects.filter(id=id).update(**updated_data)
    return JsonResponse({'upd_data': upd_data})


# Переделать, чтобы апдейтить параметры можно только по выбору
@login_required
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


@login_required
@require_POST
def tender_delete(request):
    id = request.POST.get('id')
    Tenders.objects.filter(id=id).delete()
    return JsonResponse({'remove_data': id})
