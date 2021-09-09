from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'firstapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('dashboard/', views.)
]