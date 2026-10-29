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

class Filmes(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50)
    descricao = models.TextField(verbose_name='Descrição', max_length=1000)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    cartaz = models.ImageField(upload_to='cartazes/')
    
    def __str__(self):
        return self.nome
    
class Serie(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    cartaz = models.ImageField(upload_to='cartazes/')
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    def __str__(self):
        return f"Nome: {self.nome}"
    
class Temporada(models.Model):
    nome = models.ForeignKey(
        Serie, 
        on_delete=models.CASCADE,
        related_name= 'temporadas'
    )
    numero = models.PositiveIntegerField()
    
    
class Episodios(models.Model):
    temporada = models.ForeignKey(
        Temporada,
        on_delete=models.CASCADE,
        related_name='episodios'
    )    
    numero = models.PositiveIntegerField()
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    
    def __str__(self):
        return self.titulo
        


