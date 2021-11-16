from django.urls import path

from tenders import views

urlpatterns = [
    path('tender_create/', views.tender_create, name='tender_create'),
    path('tender_delete/', views.tender_delete, name='tender_delete'),
    path('tender_update/', views.tender_update, name='tender_update'),
    path('tender_list/', views.get_tender_list, name='tender_list'),
    path('', views.tender_detail_info, name='tender_detail_info'),
]
