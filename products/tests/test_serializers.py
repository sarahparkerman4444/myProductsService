import uuid

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from . import model_factories
from ..serializer import CategorySerializer, RootCategorySerializer, ProductSerializer, PropertySerializer


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
        keys = ['id', 'uuid', 'name', 'is_global', 'create_date', 'edit_date', 'level', 'parent', ]
        self.assertEqual(set(serializer.data.keys()), set(keys))

    def test_rootcategoryserializer_keys(self):
        product_category = model_factories.CategoryFactory()
        serializer = RootCategorySerializer(product_category)
        keys = ['id', 'uuid', 'children', 'name', 'is_global', 'create_date', 'edit_date', 'level', 'parent', ]
        self.assertEqual(set(serializer.data.keys()), set(keys))


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

    def test_product_serializer(self):
        product = model_factories.Product()
        serializer = ProductSerializer(product)
        keys = ["id",
                "uuid",
                "replaced_product",
                "category_display",
                "subcategory_display",
                "part_number",
                "installation_date",
                "manufacture_date",
                "recurring_check_interval",
                "notes",
                "workflowlevel2_uuid",
                "name",
                "make",
                "model",
                "style",
                "description",
                "type",
                "file",
                "file_name",
                "status",
                "reference_id",
                "organization_uuid",
                "create_date",
                "edit_date",
                "category",
                "replacement_product",
            ]
        self.assertEqual(set(serializer.data.keys()), set(keys))


class PropertySerializerTest(TestCase):

    def test_property_serializer(self):
        product_property = model_factories.Property()
        serializer = PropertySerializer(product_property)
        keys = ["id",
                "uuid",
                "product",
                "name",
                "value",
                "type",
                "create_date",
                "edit_date",
            ]
        self.assertEqual(set(serializer.data.keys()), set(keys))
