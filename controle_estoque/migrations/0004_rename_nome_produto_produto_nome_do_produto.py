# Generated by Django 4.2.7 on 2023-11-16 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estoque', '0003_rename_preco_produto_preco_custo_produto_preco_venda'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='nome_produto',
            new_name='Nome do Produto',
        ),
    ]
