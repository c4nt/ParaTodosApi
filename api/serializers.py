from rest_framework import serializers

from .models import Usuario, Livro, Doacao, Solicitacao, Avaliacao

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        
        extra_kwargs = {
            'email' : {'write_only': True}
        }

        model = Usuario
        
        fields = (
            'id',
            'nome',
            'email',
            'senha',
        )

class LivroSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Livro
        
        fields = (
            'id',
            'titulo',
            'autor',
            'edicao',
            'conservacao',
            'dono_livro',
        )

class DoacaoSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Doacao
        
        fields = (
            'id',
            'data',
            'ativa',
            'doador',
            'livro_doado',
        )

class SolicitacaoSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Solicitacao
        
        fields = (
            'id',
            'data',
            'ativa',
            'solicitante',
            'livro_solicitado',
        )

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Avaliacao
        
        fields = (
            'id',
            'avaliacao_doador',
            'avaliacao_solicitante',
            'doador_avaliacao',
            'solicitante_avaliacao',
        )