from rest_framework import serializers

from .models import Admission, EquipmentWorker, Type


class AdmissionSerializer(serializers.ModelSerializer):
    """список поступлений"""
    id_type = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Admission
        fields = ('id_type', 'name', 'in_stock')


class InvenNumSerializer(serializers.ModelSerializer):
    """вывод инвентарного номера"""

    class Meta:
        model = EquipmentWorker
        fields = ('inven_num',)


class EquipmentTypeWorkerSerializer(serializers.ModelSerializer):
    """список поступлений"""
    admission_e = InvenNumSerializer(many=True)

    class Meta:
        model = Admission
        fields = ('name', 'admission_e')


class AdmissionDetailSerializer(serializers.ModelSerializer):
    """детали поступления"""
    # id_type = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Admission
        fields = '__all__'


class AdmissionCreateSerializer(serializers.ModelSerializer):
    """добавление записи"""

    class Meta:
        model = Admission
        fields = '__all__'


class EquipmentWorkerSerializer(serializers.ModelSerializer):
    """список поступлений"""
    id_workers = serializers.SlugRelatedField(slug_field='full_name', read_only=True)
    id_room = serializers.SlugRelatedField(slug_field='number', read_only=True)

    class Meta:
        model = EquipmentWorker
        fields = ('id_workers', 'id_room')


class EquipmentWorkerDetailSerializer(serializers.ModelSerializer):
    """детали поступления"""
    # id_workers = serializers.SlugRelatedField(slug_field='full_name', read_only=True)
    # id_room = serializers.SlugRelatedField(slug_field='number', read_only=True)
    # id_type = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # eq_name = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = EquipmentWorker
        fields = "__all__"


class EquipmentWorkerCreateSerializer(serializers.ModelSerializer):
    """обновление записей закрепленных оборудований"""

    class Meta:
        model = EquipmentWorker
        fields = '__all__'

    def create(self, validated_data):
        rating = EquipmentWorker.objects.update_or_create(
            inven_num = validated_data.get('inven_num', None),
            defaults={'date': validated_data.get('date'),
                      'upload': validated_data.get('upload'),
                      'eq_name': validated_data.get('eq_name'),
                      'id_type': validated_data.get('id_type'),
                      'id_workers': validated_data.get('id_workers'),
                      'id_room': validated_data.get('id_room')
                      }

        )
        print(rating)
        return rating



class TypeEquipmentListSerializer(serializers.ModelSerializer):
    """типы оборудования"""
    type = EquipmentTypeWorkerSerializer(many=True)

    class Meta:
        model = Type
        fields = ('id', 'name', 'type')

