from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Series, Filmes
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseView(LoginRequiredMixin, ListView):
    template_name = 'base_plataform.html'
    model = Series
    context_object_name = 'series'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filmes'] = Filmes.objects.all()
        
        return context

class SeriesModal(LoginRequiredMixin, DetailView):
    template_name = 'modal.html'
    model = Series
    context_object_name = 'series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modal_tipo'] = "series"
        return context


class FilmeModal(LoginRequiredMixin, DetailView):
    model = Filmes
    template_name = 'modal.html'
    context_object_name = 'filme'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modal_tipo'] = "filme"
        return context
