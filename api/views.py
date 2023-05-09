from rest_framework import generics

from .models import Usuario, Livro, Doacao, Solicitacao, Avaliacao
from .serializers import UsuarioSerializer, LivroSerializer, DoacaoSerializer, SolicitacaoSerializer, AvaliacaoSerializer

class UsuariosAPIView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LivrosAPIView(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class DoacoesAPIView(generics.ListCreateAPIView):
    queryset = Doacao.objects.all()
    serializer_class = DoacaoSerializer

class SolicitacoesAPIView(generics.ListCreateAPIView):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class UsuarioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class LivroAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class DoacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doacao.objects.all()
    serializer_class = DoacaoSerializer

class SolicitacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer