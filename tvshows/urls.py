from django.urls import path
from . import views

urlpatterns = [
    path('', views.filmListView, name='filmList'),
    path('film_detail/<int:id>/', views.filmDetailView, name='detail'),
    path('film_detail/<int:id>/delete/', views.deleteFilmView, name='delete'),
    path('film_detail/<int:id>/update/', views.updateFilmView, name='update'),
    path('create_film/', views.createFilmView, name='createFilm'),
    path('movie-schedule/', views.movie_schedule, name='movie_schedule'),
]