from django.contrib import admin
from django.urls import path
from .views import FilmeModal, SeriesModal, BaseView

urlpatterns = [
    path('plataform/', BaseView.as_view(), name='base'),
    path("filme/<int:pk>/modal/",FilmeModal.as_view(), name='filme_modal'),
    path("series/<int:pk>/modal/", SeriesModal.as_view(), name='series_modal'),
]