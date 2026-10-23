from django.db import models

CATEGORIA_CHOICES = {
    
    "Ação":"Ação",
    "Comédia":"Comédia",
    "Drama":"Drama",
    "Terror":"Terror",
    "Ficção Científica":"Ficção Científica",
    "Romance": "Romance",
    "Suspense":"Suspence"
}

TEMPORADAS_CHOICES = {
    "Temporada 1": "Temporada 1",
    "Temporada 2": "Temporada 2",
    "Temporada 3": "Temporada 3",
    "Temporada 4": "Temporada 4",
    "Temporada 5": "Temporada 5",
    "Temporada 6": "Temporada 6",
    "Temporada 7": "Temporada 7",
    "Temporada 8": "Temporada 8",
    "Temporada 9": "Temporada 9",
    "Temporada 10": "Temporada 10",
    "Temporada 11": "Temporada 11",
    "Temporada 12": "Temporada 12",
    "Temporada 13": "Temporada 13",
    "Temporada 14": "Temporada 14",
    "Temporada 15": "Temporada 15",
    "Temporada 16": "Temporada 16",
    "Temporada 17": "Temporada 17",
    "Temporada 18": "Temporada 18",
}


class Filmes(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50)
    descricao = models.TextField(verbose_name='Descrição', max_length=1000)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    cartaz = models.ImageField(upload_to='cartazes/')
    
    def __str__(self):
        return self.nome
    
class Nome_da_serie(models.Model):
    nome_da_serie = models.CharField(verbose_name='Nome da Série', max_length=50)
    
    def __str__(self):
        return f"Nome: {self.nome_da_serie}"
    
    
class Series(models.Model):
    nome_da_serie = models.ForeignKey(Nome_da_serie, on_delete=models.PROTECT, related_name="episodios")
    episodio = models.CharField(max_length=30)
    temporada = models.CharField(max_length=20, choices=TEMPORADAS_CHOICES)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    cartaz = models.ImageField(upload_to='cartazes/')
    
    def __str__(self):
        return f"Série: {self.nome_da_serie} | Episódio: {self.episodio} | Temporada: {self.temporada}"   
     


