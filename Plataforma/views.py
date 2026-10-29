from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Episodios, Filmes, Serie, Temporada
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch


class BaseView(LoginRequiredMixin, ListView):
    template_name = 'base_plataform.html'
    model = Serie
    context_object_name = 'series'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filmes'] = Filmes.objects.all()

        return context

class SeriesModal(LoginRequiredMixin, DetailView):
    template_name = 'modalSeries.html'
    model = Serie
    context_object_name = 'serie'
    def get_queryset(self):
        temporadas = Prefetch(
            'temporadas', Temporada.objects.order_by('numero').prefetch_related(
                Prefetch('episodios', queryset=Episodios.objects.order_by('numero')
                         )))
        return Serie.objects.prefetch_related(temporadas)

class FilmeModal(LoginRequiredMixin, DetailView):
    model = Filmes
    template_name = 'modal.html'
    context_object_name = 'filme'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modal_tipo'] = "filme"
        return context
