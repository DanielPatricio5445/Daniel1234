from django.contrib import admin
from .models import Usuario, Produto, Categoria

# Configuração do admin para Usuario
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "senha")

# Configuração do admin para Produto
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "descricao", "preco", "foto", "estoque", "categoria")

# Configuração do admin para Categoria
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)

# Registro dos modelos no admin
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
