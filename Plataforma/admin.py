from django.contrib import admin
from .models import Filmes, Series, Nome_da_serie

class FilmesAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'categoria', 'cartaz']
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['nome_da_serie', 'episodio', 'temporada', 'categoria', 'cartaz']
class NomeDaSerieAdmin(admin.ModelAdmin):
    list_display = ['nome_da_serie',]
    
admin.site.register(Filmes, FilmesAdmin)
admin.site.register(Nome_da_serie, NomeDaSerieAdmin)
admin.site.register(Series, SeriesAdmin )