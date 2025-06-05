from django.urls import path
from . import views

urlpatterns = [
    # Rotas principais
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),

    # Rotas de Usuário
    path('usuarios/', views.exibirUsuarios, name='exibirUsuarios'),
    path('add-usuario/', views.addUsuario, name='addUsuario'),
    path('editar-usuario/<int:id_usuario>/', views.editarUsuario, name='editarUsuario'),
    path('excluir-usuario/<int:id_usuario>/', views.excluirUsuario, name='excluirUsuario'),

    # Rotas de Produto
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produtos/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('produtos_card/', views.produtos_card, name='produtos_card'),

    # Novas rotas para checkout e confirmação
    path('checkout/<int:id_produto>/', views.checkout, name='checkout'),
    path('confirmacao/', views.confirmacao, name='confirmacao'),

    path('grafico', views.grafico, name="grafico"), 

    path('categorias', views.getCategorias, name="categorias"),

    path('categoria/<int:id_categoria>/', views.getCategoriaID, name="categoriaID"),
]

