from django.shortcuts import redirect, render
from .forms import Form_Produto
from .models import Produto

# Create your views here.

def home_page(request):
    return render(request, "home.html")


def consulta_page(request):
    lista_de_produtos = Produto.objects.all().order_by("nome_produto")
    context = {
        "lista_de_produtos": lista_de_produtos
    }
    return render(request, "consulta.html", context)

def consulta_item(request, id_item):
    produto = Produto.objects.get(pk = id_item)
    form = Form_Produto(instance=produto)
    context = {
        "produto": produto,
        "form": form,
    }
    return render(request, "consulta_item.html", context)

def editar_item(request, id_item):
    produto = Produto.objects.get(pk = id_item)
    
    if request.POST:
        form = Form_Produto(request.POST, instance=produto)
        form.save()
        return redirect(f"/ConsultaItem/{produto.id}")
    
    form = Form_Produto(instance=produto)
    context = {
        "produto": produto,
        "form": form,
    }
    return render(request, "editar_item.html", context)

def delete_item(request, id_item):
    produto = Produto.objects.get(pk = id_item)
    
    if request.POST:
        produto.delete()
    
    return redirect(f"/Consulta")

def cadastro_page(request):
    if request.POST:
        form = Form_Produto(request.POST)
        form.save()
        print("Formulário salvo com sucesso.")
    form = Form_Produto()

    context = {
        "form": form
    }
    return render(request, "cadastro.html", context)
