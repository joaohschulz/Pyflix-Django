from django.contrib import admin
from .models import Filmes, Serie, Temporada, Episodio

class FilmesAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'categoria', 'cartaz']
class SerieAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'categoria', 'cartaz']
class TemporadaAdmin(admin.ModelAdmin):
    list_display = ['serie', 'numero']
class EpisodioAdmin(admin.ModelAdmin):
    list_display = ['temporada', 'numero', 'titulo', 'descricao']
    
    
admin.site.register(Filmes, FilmesAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Temporada, TemporadaAdmin)
admin.site.register(Episodio, EpisodioAdmin)