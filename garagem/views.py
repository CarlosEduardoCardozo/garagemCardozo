from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria, Cor, Acessorio, Modelo, Veiculo
from garagem.serializers import CategoriaSerializer, CorSerializer, AcessorioSerializer, ModeloSerializer, VeiculoSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
    
class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

