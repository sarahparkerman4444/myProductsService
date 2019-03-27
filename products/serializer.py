from django.urls import reverse

from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    replaced_product = serializers.PrimaryKeyRelatedField(queryset=models.Product.objects.all(), required=False,
                                                          allow_null=True)

    def to_representation(self, instance):
        # replace direct file link with file entry point URL
        data = super().to_representation(instance)
        data['file'] = reverse('product-file', args=(instance.uuid,)) \
            if data['file'] else None
        return data

    def update(self, product: models.Product, validated_data: dict):
        product = super().update(product, validated_data)
        if 'replaced_product' in validated_data.keys():
            return product.set_replaced_product(validated_data['replaced_product'])
        return product

    def create(self, validated_data):
        file_data = validated_data.get('file')
        if file_data and not validated_data.get('file_name'):
            validated_data['file_name'] = file_data.name
        product = super().create(validated_data)
        if 'replaced_product' in validated_data.keys():
            return product.set_replaced_product(validated_data['replaced_product'])
        return product

    class Meta:
        model = models.Product
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Property
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        exclude = ('organization_uuid', )
