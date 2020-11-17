from django.urls import path
from . import views

urlpatterns = [
    path('coupon/', views.coupon),
    path('class5/', views.class5),
    # path('coupon/use/', views.use_coupon),
]