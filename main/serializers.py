"""Сериализаторы всея моделей"""

from rest_framework import serializers
from rest_framework.serializers import ListSerializer

from main.models import Offer, WeightDimension, Timing, ProcessingState, ProcessingStateNote, \
    Mapping


class WeightDimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightDimension
        fields = ['length', 'width', 'height', 'weight']


class TimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timing
        fields = ['timePeriod', 'timeUnit', 'comment']


class ProcessingStateNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessingStateNote
        fields = ['payload', 'type']


class ProcessingStateSerializer(serializers.ModelSerializer):
    notes = ProcessingStateNoteSerializer()

    class Meta:
        model = ProcessingState
        fields = ['status', 'notes']


class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping
        fields = ['marketSku', 'modelId', 'categoryId']


class OfferSerializer(serializers.ModelSerializer):
    weightDimensions = WeightDimensionSerializer()
    manufacturerCountries = ListSerializer(child=serializers.CharField())
    urls = ListSerializer(child=serializers.CharField())
    barcodes = ListSerializer(child=serializers.CharField())
    shelfLife = TimingSerializer()
    lifeTime = TimingSerializer()
    guaranteePeriod = TimingSerializer()
    customsCommodityCodes = ListSerializer(child=serializers.CharField())
    supplyScheduleDays = ListSerializer(child=serializers.CharField())
    processingState = ProcessingStateSerializer()
    mapping = MappingSerializer()
    awaitingModerationMapping = MappingSerializer()
    rejectedMapping = MappingSerializer()

    class Meta:
        model = Offer
        fields = [
            'id',
            'shopSku',
            'name',
            'category',
            'manufacturer',
            'weightDimensions',
            'manufacturerCountries',
            'urls',
            'barcodes',
            'description',
            'shelfLife',
            'lifeTime',
            'guaranteePeriod',
            'customsCommodityCodes',
            'certificate',
            'availability',
            'transportUnitSize',
            'minShipment',
            'quantumOfSupply',
            'supplyScheduleDays',
            'deliveryDurationDays',
            'boxCount',
            'shelfLifeDays',
            'lifeTimeDays',
            'guaranteePeriodDays',
            'processingState',
            'mapping',
            'awaitingModerationMapping',
            'rejectedMapping'
        ]