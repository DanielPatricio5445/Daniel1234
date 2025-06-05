from django import forms
from app.models import Usuario, Produto, Venda

class formUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = (
            'nome', 'email', 'senha', 'cep', 'logradouro', 'bairro',
            'localidade', 'uf', 'numero'
        )
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CEP'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'localidade': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'uf': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número da residência'}),
        }

class formProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'preco', 'foto', 'estoque', 'categoria')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecione uma categoria'}),
        }

class formLogin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('email', 'senha')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control'})
        }

class formVenda(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ('numero_cartao', 'validade', 'cvv')
        widgets = {
            'numero_cartao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número do cartão'
            }),
            'validade': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'MM/AA'
            }),
            'cvv': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CVV'
            }),
        }
