from django.urls import path

from .views import UsuariosAPIView, LivrosAPIView, DoacoesAPIView, SolicitacoesAPIView, AvaliacoesAPIView, UsuarioAPIView, LivroAPIView, DoacaoAPIView, SolicitacaoAPIView, AvaliacaoAPIView

urlpatterns = [
    path('usuarios/', UsuariosAPIView.as_view(), name='usuarios'),
    path('livros/', LivrosAPIView.as_view(), name='livros'),
    path('doacoes/', DoacoesAPIView.as_view(), name='doacoes'),
    path('solicitacoes/', SolicitacoesAPIView.as_view(), name='solicitacoes'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),

    path('usuario/<int:pk>/', UsuarioAPIView.as_view(), name='usuario'),
    path('livro/<int:pk>/', LivroAPIView.as_view(), name='livro'),
    path('doacao/<int:pk>/', DoacaoAPIView.as_view(), name='doacao'),
    path('solicitacao/<int:pk>/', SolicitacaoAPIView.as_view(), name='solicitacao'),
    path('avaliacao/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),

]