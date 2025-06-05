from django.shortcuts import render, redirect, get_object_or_404
from app.models import Usuario, Produto, Venda, Categoria
from app.forms import formUsuario, formProduto, formLogin, formVenda
from datetime import timedelta
import requests
import io, urllib, base64
import matplotlib.pyplot as plt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategoriaSerializer


# Página inicial
def home(request):
    return render(request, "template.html")

# ========== USUÁRIOS ==========

# Exibir todos os usuários
def exibirUsuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuario.html", {'listUsuarios': usuarios})

# Adicionar novo usuário
def addUsuario(request):
    if request.method == "POST":
        formUser = formUsuario(request.POST)
        if formUser.is_valid():
            formUser.save()
            print("Usuário cadastrado com sucesso!")
            return redirect('exibirUsuarios')
        else:
            print("Formulário inválido:", formUser.errors)
    else:
        formUser = formUsuario()

    return render(request, "add-usuario.html", {'form': formUser})

# Editar usuário
def editarUsuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    formUser = formUsuario(request.POST or None, instance=usuario)

    if request.method == "POST":
        if formUser.is_valid():
            formUser.save()
            return redirect("exibirUsuarios")

    return render(request, "editar-usuario.html", {'form': formUser})

# Excluir usuário
def excluirUsuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.delete()
    return redirect("exibirUsuarios")

# ========== PRODUTOS ==========

# Listar produtos
def listar_produtos(request):
    if request.session.get("email") is None:
        return redirect('login')
    produtos = Produto.objects.all()
    return render(request, "produtos/listar_produtos.html", {'produtos': produtos})

# Cadastrar produto
def cadastrar_produto(request):
    if request.method == 'POST':
        form = formProduto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = formProduto()
    return render(request, 'produtos/cadastrar_produto.html', {'form': form})

# Editar produto
def editar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    if request.method == 'POST':
        form = formProduto(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = formProduto(instance=produto)
    return render(request, 'produtos/editar_produto.html', {'form': form})

# Excluir produto
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()
    return redirect('listar_produtos')

# ========== LOGIN ==========

def login(request): 
    frmLogin = formLogin(request.POST or None)
    if request.POST: 
        if frmLogin.is_valid():
            _email = frmLogin.cleaned_data.get('email')
            _senha = frmLogin.cleaned_data.get('senha')
            try:
                userLogin = Usuario.objects.get(email=_email, senha=_senha)
                if userLogin is not None:
                    request.session.set_expiry(timedelta(seconds=60))
                    request.session["email"] = userLogin.email
                    return redirect('dashboard')
            except Usuario.DoesNotExist:
                return render(request, "login.html", {'form': frmLogin, 'error': 'Usuário ou senha inválidos.'})
    return render(request, "login.html", {'form': frmLogin})

def dashboard(request):
    _email = request.session.get("email")
    return render(request, "dashboard.html", {'email': _email})

def quem_somos(request):
    return render(request, "quem_somos.html")

# Produtos da API (sem botão de compra)
def produtos_card(request):
    produtos = Produto.objects.all()
    produtosapi = requests.get("https://fakestoreapi.com/products").json()
    return render(request, "produtos/produtos_card.html", {'produtos':produtosapi})

# ========== COMPRAS ==========

def checkout(request, id_produto):
    if request.session.get("email") is None:
        return redirect('login')
    
    produto = get_object_or_404(Produto, pk=id_produto)
    cliente = get_object_or_404(Usuario, email=request.session.get("email"))

    if request.method == "POST":
        form = formVenda(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)
            venda.cliente = cliente
            venda.produto = produto
            venda.preco_venda = produto.preco
            venda.save()
            return redirect('confirmacao')
    else:
        form = formVenda()

    return render(request, 'produtos/checkout.html', {
        'form': form,
        'produto': produto,
        'cliente': cliente
    })

def confirmacao(request):
    return render(request, 'produtos/confirmacao.html')

def grafico(request):
    produtos = Produto.objects.all()
    nome = [produto.nome for produto in produtos]
    estoque = [produto.estoque for produto in produtos]

    fig, ax = plt.subplots()
    ax.bar(nome, estoque)
    ax.set_xlabel("Produto")
    ax.set_ylabel("Estoque")
    ax.set_title("Produtos")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)

    return render(request, 'grafico.html', {'dados': uri})

@api_view(['GET','POST'])
def getCategorias(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategoriaSerializer(data=request.data)
        if serializer.isValid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def getCategoriaID(request, id_categoria):
    try:
        categoria =  Categoria.objects.get(id=id_categoria)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    






