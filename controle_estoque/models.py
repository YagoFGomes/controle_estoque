from django.db import models

class Categoria(models.Model):
    nome_categoria= models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return self.nome_categoria
    

class Produto(models.Model):
    nome_produto= models.CharField(max_length=200, blank=False, null=False)
    codigo_produto= models.CharField(max_length=200, blank=False, null=False)
    quantidade= models.BigIntegerField(default=0)
    quantidade_minima= models.BigIntegerField(default=0)
    categoria= models.ForeignKey(to=Categoria, on_delete=models.PROTECT)
    preco_custo= models.FloatField(blank=False, null=False)
    preco_venda= models.FloatField(blank=False, null=False)

    def __str__(self):
        return f"{self.nome_produto} - Cód. {self.codigo_produto}"
    