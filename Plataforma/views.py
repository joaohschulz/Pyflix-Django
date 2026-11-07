from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Serie, Filmes
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseView(LoginRequiredMixin, ListView):
    template_name = 'base_plataform.html'
    model = Serie
    context_object_name = 'series'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filmes'] = Filmes.objects.all()
        
        return context

class SeriesModal(LoginRequiredMixin, DetailView):
    template_name = 'modal.html'
    model = Serie
    context_object_name = 'serie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modal_tipo'] = "series"
        return context
    
    def get_queryset(self):
        return Serie.objects.prefetch_related('temporadas__episodios')


class FilmeModal(LoginRequiredMixin, DetailView):
    model = Filmes
    template_name = 'modal.html'
    context_object_name = 'filme'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modal_tipo'] = "filme"
        return context
