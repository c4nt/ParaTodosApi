from django.contrib import admin

from .models import Usuario, Livro, Doacao, Solicitacao, Avaliacao

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin) :
    list_display = ('id','nome','email','senha',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin) :
    list_display = ('id','titulo','autor','edicao','conservacao','dono_livro',)

@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin) :
    list_display = ('id','data','ativa','doador','livro_doado',)

@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin) :
    list_display = ('id','data','ativa','solicitante','livro_solicitado',)

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin) :
    list_display = ('id','avaliacao_doador','avaliacao_solicitante','doador_avaliacao','solicitante_avaliacao',)
