from django.urls import path, register_converter, re_path
from .converters import FourDigitYearConverter
from . import views

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'shop'

urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year),
    path('', views.item_list),
    path('<int:pk>/', views.item_detail),
    # 위의 path 문법과 동일한 역할
    # re_path(r'^(?P<pk>\d+)/$', views.item_detail),
]
