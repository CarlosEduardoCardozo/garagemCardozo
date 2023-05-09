from rest_framework.serializers import ModelSerializer

from garagem.models import Categoria, Cor, Acessorio, Modelo, Veiculo


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"

class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"