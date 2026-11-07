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
        return f'Filmes: {self.nome}'
    
class Serie(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    cartaz = models.ImageField(upload_to='cartazes/')
    def __str__(self):
        return f'Serie: {self.nome}'
    
class Temporada(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='temporadas') 
    numero = models.PositiveIntegerField()
    class Meta:
        # para não ficar usando order_by toda vez
        ordering = ['numero']
    def __str__(self):
        return f'{self.serie.nome} -- Temporada {self.numero}'

class Episodio(models.Model):
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE, related_name='episodios')
    numero = models.PositiveIntegerField()
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    class Meta:
        ordering = ['numero']
    
    def __str__(self):
        return f'{self.temporada} -- Ep. {self.numero}: {self.titulo}'
