from django import forms
from .models import Produto

class Form_Produto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = "__all__"
        labels = {
                'nome_produto': 'Nome do Produto',
                'codigo_produto': 'Codigo do Produto',
                'quatidade': 'Quantidade',
                'quantidade_minima': 'Quantidade Mínima',
                'categoria': 'Categoria',
                'preco_custo': 'Preço do Produto',
                'preco_venda' : 'Preço de Venda'
        }