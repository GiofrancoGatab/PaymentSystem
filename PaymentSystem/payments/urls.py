from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('add/', views.add_payment, name='add_payment'),
    path('edit/<int:id>/', views.edit_payment, name='edit_payment'),
    path('delete/<int:id>/', views.delete_payment, name='delete_payment'),
    path('report/', views.payment_report, name='payment_report'),
    path('', views.payment_report, name='payment_list'),
    path('add/', views.add_payment, name='add_payment'),
]
