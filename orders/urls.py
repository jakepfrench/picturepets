from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='orders'),
    path('new/', views.new_order, name='new_order'),
]
