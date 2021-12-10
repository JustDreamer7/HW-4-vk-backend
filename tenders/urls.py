from django.urls import path
from django.conf.urls import url
from .views import TenderView
from tenders import views

# urlpatterns = [
#     path('tender_create/', views.tender_create, name='tender_create'),
#     path('tender_delete/', views.tender_delete, name='tender_delete'),
#     path('tender_update/', views.tender_update, name='tender_update'),
#     path('tender_list/', views.tender_list, name='tender_list'),
#     path('', views.tender_detail_info, name='tender_detail_info'),
# ]


urlpatterns = [
    url(
        regex=r'^api/list/$',
        view=TenderView.as_view({'get': 'list'}),
        name='tender-list'
    ),
]