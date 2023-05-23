from django.urls import path

from . import views


app_name = 'concerts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:concert_id>/', views.detail, name='detail'),

    path('db_info/', views.db_info, name='db_info'),

    path('add_genre/', views.addGenre, name='add_genre'),
    path('update_genre/<int:genre_id>/', views.updateGenre, name='update_genre'),
    path('delete_genre/<int:genre_id>/', views.deleteGenre, name='delete_genre'),

    path('add_artist/', views.addArtist, name='add_artist'),
    path('update_artist/<int:artist_id>/', views.updateArtist, name='update_artist'),
    path('delete_artist/<int:artist_id>/', views.deleteArtist, name='delete_artist'),

    path('add_typeofplace/', views.addTypeofplace, name='add_typeofplace'),
    path('update_typeofplace/<int:typeofplace_id>/', views.updateTypeofplace, name='update_typeofplace'),
    path('delete_typeofplace/<int:typeofplace_id>/', views.deleteTypeofplace, name='delete_typeofplace'),

    path('add_place/', views.addPlace, name='add_place'),
    path('update_place/<int:place_id>/', views.updatePlace, name='update_place'),
    path('delete_place/<int:place_id>/', views.deletePlace, name='delete_place'),

    path('add_concert/', views.addConcert, name='add_concert'),
    path('update_concert/<int:concert_id>/', views.updateConcert, name='update_concert'),
    path('delete_concert/<int:concert_id>/', views.deleteConcert, name='delete_concert'),
]