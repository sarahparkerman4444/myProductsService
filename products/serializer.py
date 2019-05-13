from django.urls import reverse

from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    replaced_product = serializers.PrimaryKeyRelatedField(queryset=models.Product.objects.all(), required=False,
                                                          allow_null=True)
    category_display = serializers.SerializerMethodField(method_name='get_root_category_display')
    subcategory_display = serializers.SerializerMethodField(method_name='get_level1_category_display')

    def get_root_category_display(self, obj):
        if obj.category:
            if getattr(obj.category, 'parent', None):
                return obj.category.parent.name
            return obj.category.name
        return None

    def get_level1_category_display(self, obj):
        if obj.category and getattr(obj.category, 'parent', None):
            return obj.category.name
        return None

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
        read_only_fields = (
            'organization_uuid',
        )


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Property
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        exclude = (
            'organization_uuid',
        )


class RootCategorySerializer(CategorySerializer):
    children = CategorySerializer(many=True, read_only=True)
