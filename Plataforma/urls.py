from django.contrib import admin
from django.urls import path
from .views import FilmeModal, PlayerEpisodioView, PlayerView, SeriesModal, BaseView

urlpatterns = [
    path('plataform/', BaseView.as_view(), name='base'),
    path("filme/<int:pk>/modal/",FilmeModal.as_view(), name='filme_modal'),
    path("series/<int:pk>/modal/", SeriesModal.as_view(), name='series_modal'),
    path("player/<int:pk>/", PlayerView.as_view(), name='player'),
    path("episodio/<int:pk>/player/", PlayerEpisodioView.as_view(), name='episodio_player'),
]