from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField('Email')
    senha = models.CharField(max_length=30)

class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    edicao = models.CharField(max_length=150)
    conservacao = models.IntegerField(null=False)
    dono_livro = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='dono_do_livro')
    
class Doacao(models.Model):
    data = models.DateField(auto_now_add=True)
    ativa =  models.BooleanField(default=True)
    doador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='doador_do_livro')
    livro_doado = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='livro_doado')

class Solicitacao(models.Model):
    data = models.DateField(auto_now_add=True)
    ativa =  models.BooleanField(default=True)
    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitante_do_livro')
    livro_solicitado = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='livro_solicitado')


class Avaliacao(models.Model):
    avaliacao_doador = models.DecimalField(max_digits=2,decimal_places=2)
    avaliacao_solicitante = models.DecimalField(max_digits=2,decimal_places=2)
    doador_avaliacao = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='doador')
    solicitante_avaliacao = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitante')