# Generated by Django 4.2.7 on 2023-11-16 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estoque', '0004_rename_nome_produto_produto_nome_do_produto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='Nome do Produto',
            new_name='nome_produto',
        ),
    ]
