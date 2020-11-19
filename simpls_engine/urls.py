from django.urls import path

from . import views

app_name = 'simpls_engine'
urlpatterns = [
    path('', views.index, name='index'),
]