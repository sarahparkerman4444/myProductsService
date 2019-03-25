import uuid

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from . import model_factories
from ..serializer import ProductCategorySerializer


class ProductCategorySerializerTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = model_factories.User()
        self.organization_uuid = str(uuid.uuid4())
        self.session = {
            'jwt_organization_uuid': self.organization_uuid,
        }

    def test_productcategoryserializer_keys(self):
        product_category = model_factories.ProductCategoryFactory()
        serializer = ProductCategorySerializer(product_category)
        keys = ['id', 'name', 'is_global', 'create_date', 'edit_date', ]
        self.assertEqual(list(serializer.data.keys()), keys)
