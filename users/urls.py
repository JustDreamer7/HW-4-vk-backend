from django.urls import path
from users import views
from django.conf.urls import url
from .views import UserView
# urlpatterns = [
#     path('user_create/', views.user_create, name='user_create'),
#     path('user_delete/', views.user_delete, name='user_delete'),
#     path('user_update/', views.user_update, name='user_update'),
#     path('user_list/', views.get_user_list, name='user_list'),
#     path('', views.user_detail_info, name='user_detail_info')
# ]
urlpatterns = [
    url(
        regex=r'^api/list/$',
        view=UserView.as_view({'get': 'list'}),
        name='user-list'
    ),
]