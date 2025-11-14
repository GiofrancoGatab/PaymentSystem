from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/payments/')),
    path('admin/', admin.site.urls),
    path('payments/', include('payments.urls')),
]

