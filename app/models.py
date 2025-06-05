from django.db import models

# Model para categorias
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome}"

# Model para usuários
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=16)

    cep = models.CharField(max_length=9, blank=True, null=True)
    logradouro = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    localidade = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nome

# Model para produtos
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    foto = models.ImageField(upload_to='produtos/')
    estoque = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

# Model para vendas
class Venda(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco_venda = models.DecimalField(max_digits=8, decimal_places=2)
    numero_cartao = models.CharField(max_length=16)
    validade = models.CharField(max_length=5)  # formato MM/AA
    cvv = models.CharField(max_length=4)
    data_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda de {self.produto.nome} para {self.cliente.nome}"
