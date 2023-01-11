from django.urls import path, include
from . import views

urlpatterns = [


    path('', views.static, name="static")
]
