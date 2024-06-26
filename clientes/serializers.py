from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Numero de cpf invalido!"}) 
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':" Este campo nao deve conter numeros !"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':" O RG deve conter 9 numeros !"})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':" O campo celular não é valido! Ex: 12 12345-1234"})
        
        return data
    
    
    
    
    
    