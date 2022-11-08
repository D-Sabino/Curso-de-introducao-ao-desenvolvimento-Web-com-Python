from django.urls import path
from .views import PaginaInicial

urlpatterns = [
    # path('endereco/', MinhaView.as_view(), name='nome_da_url'),
    path('', PaginaInicial.as_view(), name='inicio'),
    
]