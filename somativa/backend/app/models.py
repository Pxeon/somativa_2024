from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class CustomUser(AbstractBaseUser,PermissionsMixin):
    nome = models.CharField(max_length=70)
    email = models.EmailField("endereço de email", unique=True)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default=True)
    telefone = models.CharField(max_length=15, null= True, blank=True)
    endereço = models.CharField(max_length=50)
    cpf = models.IntegerField(max_length=11)


class CategoriaLivros(models.Model):
    nome = models.CharField(max_length=150)

    def __strl__(self):
        return self.nome
    
FORMATO_LIVRO = [
     ("E", "EBOOK"),
     ("F", "FISICO"),
]

class Livros(models.Model):
    categoriaFK = models.ForeignKey(CategoriaLivros, related_name='categoriaLivros', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    capa = models.ManyToManyField(foto)
    descricao = models.CharField(max_length=300)
    numeroPaginas = models.IntegerField()
    formato = models.CharField(max_length=6, choices= FORMATO_LIVRO)
    numeroEdicao = models.IntegerField()
    autor = models.CharField(max_length=100)
    anoPubli = models.DateField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __strl__(self):
        return self.titulo

class Emprestimos(models.Model):
    livroFK = models.ForeignKey(Livros, related_name='livrosEmprestimos', on_delete=models.CASCADE)
    usuarioFK = models.ForeignKey(CustomUser, related_name='usuarioEmprestimos', on_delete=models.CASCADE)

    def __strl__(self):
        return self.usuarioFK.nome

class Autor(models.Model):
    nome = models.CharField(max_length=80)
    foto = models.ManyToManyField(foto)
    biografia = models.CharField(max_length=500)

STATUS_LIVRO= [
     ("P", "PENDENTE"),
     ("R", "RECUSADO"),
     ("A", "APROVADO"),
]

class StatusLivro(models.Model):
    status = models.CharField(max_length=8, choices=STATUS_LIVRO)

class Carrinho(models.Model):
    usuarioFK = models.ForeignKey(CustomUser, related_name='usuarioCarrinho', on_delete=models.CASCADE)
    livroFK = models.ForeignKey(Livros, related_name='livrosCarrinho', on_delete=models.CASCADE)
