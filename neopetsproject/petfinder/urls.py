from django.urls import path

from . import views

app_name = 'petfinder'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]