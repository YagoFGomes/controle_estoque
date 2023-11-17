"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from controle_estoque.views import home_page, consulta_page, cadastro_page, consulta_item, editar_item, delete_item

urlpatterns = [
    
    path('HomePage', home_page, name="home_page"),
    path('Consulta', consulta_page, name="consulta_page"),
    path('Cadastro', cadastro_page, name="cadastro_page"),
    path('ConsultaItem/<int:id_item>', consulta_item, name="consulta_item"),
    path('EditarItem/<int:id_item>', editar_item, name="editar_item"),
    path('DeleteItem/<int:id_item>', delete_item, name="delete_item"),
    path('admin/', admin.site.urls),
]
