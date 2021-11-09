from django.urls import path
from tenders import views

urlpatterns = [
    path('', views.tender_detail, name='tender_detail'),
    path('tender_create/', views.tender_create, name='tender_create'),
    path('tender_list/', views.tender_list, name='tender_list'),
]
