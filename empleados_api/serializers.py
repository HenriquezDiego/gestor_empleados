
from rest_framework import serializers
from .models import Empleado, Area, SubArea

class EmpleadoSerializer(serializers.ModelSerializer):
    subarea_nombre = serializers.CharField(source='subarea.nombre', read_only=True)
    area = serializers.IntegerField(source='subarea.area_id', read_only=True)
    class Meta:
        model = Empleado
        fields = ['empleado_id','documento_identidad','nombres','apellidos','subarea','subarea_nombre','area']

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class SubAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubArea
        fields = '__all__'
