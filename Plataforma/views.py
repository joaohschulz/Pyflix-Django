from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Episodio, Serie, Filmes
from django.contrib.auth.mixins import LoginRequiredMixin

# aq está a baseview, ela vai renderizar a página base da plataforma, 
# que é a página inicial, onde vai ter os filmes e as séries
class BaseView(LoginRequiredMixin, ListView):
    template_name = 'base_plataform.html'
    model = Serie
    context_object_name = 'series'
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filmes'] = Filmes.objects.all()
        
        return context
# a seriesmodal é a view q vai mostrar o modal da serie, vai buscar no banco de dados a serie
# e as temporadas
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

# a mesma coisa da seriesmodal, mas para o filme, 
class FilmeModal(LoginRequiredMixin, DetailView):
    model = Filmes
    template_name = 'modal.html'
    context_object_name = 'filme'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modal_tipo'] = "filme"
        return context
   
   
   
# a partir daq estao as views de player, eu usei o contextdata, para passar valores universais no 
# template, ao inves de colocar filme.nome, filme.categoria...... e coloquei {{ categoria }} {{cartaz}}
# .... etc ... isso serve para q eu possa usar o mesmo template para o player de filme e de series
   
    
# a playerview é a view que vai mostrar o player do filme
class PlayerView(LoginRequiredMixin, DetailView):
    model = Filmes
    template_name = 'player.html'
    context_object_name = 'filme'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # o self.object é o objeto que está sendo visualizado       
        filme = self.object
        context['titulo'] = filme.nome
        context['categoria'] = filme.categoria
        context['video'] = filme.video
        context['cartaz'] = filme.cartaz
        return context
    
class PlayerEpisodioView(LoginRequiredMixin, DetailView):
    model = Episodio
    template_name = 'player.html'
    context_object_name = 'episodio'

    # o queryset é o conjunto de objetos que a view vai trabalhar
    def get_queryset(self):
        return Episodio.objects.select_related('temporada__serie')
    
    # o self.object é o objeto que está sendo visualizado
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        episodio = self.object
        context['titulo'] = episodio.titulo
        context['categoria'] = episodio.temporada.serie.categoria
        context['video'] = episodio.video
        context['cartaz'] = episodio.temporada.serie.cartaz
        return context