import uuid

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from . import model_factories
from ..serializer import CategorySerializer, RootCategorySerializer, ProductSerializer


class ProductSerializerBaseTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = model_factories.User()
        self.organization_uuid = str(uuid.uuid4())
        self.session = {
            'jwt_organization_uuid': self.organization_uuid,
        }


class ProductCategorySerializerTest(ProductSerializerBaseTest):

    def test_categoryserializer_keys(self):
        product_category = model_factories.CategoryFactory()
        serializer = CategorySerializer(product_category)
        keys = ['uuid', 'name', 'is_global', 'create_date', 'edit_date', 'level', 'parent', ]
        self.assertEqual(list(serializer.data.keys()), keys)

    def test_rootcategoryserializer_keys(self):
        product_category = model_factories.CategoryFactory()
        serializer = RootCategorySerializer(product_category)
        keys = ['uuid', 'children', 'name', 'is_global', 'create_date', 'edit_date', 'level', 'parent', ]
        self.assertEqual(list(serializer.data.keys()), keys)


class ProductSerializerTest(ProductSerializerBaseTest):

    def test_category_display_none(self):
        product = model_factories.Product()
        serializer = ProductSerializer(product)
        self.assertEqual(serializer.data['category_display'], None)

    def test_category_display(self):
        # category without parent
        product_category = model_factories.CategoryFactory(name='test-without-parent')
        product = model_factories.Product(category=product_category)
        serializer = ProductSerializer(product)
        self.assertEqual(serializer.data['category_display'], product_category.name)
        # category with parent
        product_category_parent = model_factories.CategoryFactory(name='test-with-parent')
        product_category.parent = product_category_parent
        product_category.save()
        serializer = ProductSerializer(product)
        self.assertEqual(serializer.data['category_display'], product_category_parent.name)

    def test_subcategory_display(self):
        product_category_parent = model_factories.CategoryFactory(name='test-root')
        product_subcategory = model_factories.CategoryFactory(name='test-subcategory',
                                                              parent=product_category_parent)
        product = model_factories.ProductFactory(category=product_subcategory)
        serializer = ProductSerializer(product)
        self.assertEqual(serializer.data['subcategory_display'], product_subcategory.name)
        # test None
        product.category = product_category_parent
        product.save()
        serializer = ProductSerializer(product)
        self.assertEqual(serializer.data['subcategory_display'], None)
