import uuid

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from . import model_factories
from ..serializer import CategorySerializer, RootCategorySerializer


class ProductCategorySerializerTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = model_factories.User()
        self.organization_uuid = str(uuid.uuid4())
        self.session = {
            'jwt_organization_uuid': self.organization_uuid,
        }

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
