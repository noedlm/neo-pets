from django.urls import path

from . import views

app_name = 'petfinder'
urlpatterns = [
    path('add/pet/', views.addFavorite, name='add_favorite'),
    path('delete/pet/', views.deleteFavorite, name='delete_favorite'),
    path('favorites/', views.listFavorites, name="favorites"),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
]