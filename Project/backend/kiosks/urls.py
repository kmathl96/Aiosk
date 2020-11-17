from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.pay),
    path('menu_list/', views.menu_list),
    path('detect_age/', views.detect_age),
    path('recommend/', views.get_recommendation),
]