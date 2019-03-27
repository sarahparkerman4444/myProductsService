from typing import Any

from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.pagination import CursorPagination, PageNumberPagination
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
import django_filters
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import FileResponse

from products.models import Category, Property, Product
from products.permissions import OrganizationPermission
from . import serializer


class StandardResultsSetPagination(PageNumberPagination):
    max_page_size = 1000
    page_size = 100
    page_size_query_param = 'page_size'


class SmallResultsSetPagination(PageNumberPagination):
    max_page_size = 50
    page_size = 20
    page_size_query_param = 'page_size'


class DefaultCursorPagination(CursorPagination):
    max_page_size = 100
    page_size = 30
    page_size_query_param = 'page_size'


class ProductViewSet(viewsets.ModelViewSet):
    """
    Product viewset is used to create list or inventory of products or THINGS
    to be tracked and related to a project.

    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    # Remove CSRF request verification for posts to this API
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ProductViewSet, self).dispatch(*args, **kwargs)

    def list(self, request):
        # Use this queryset or the django-filters lib will not work
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def file(self, request, *args, **kwargs):
        product = self.get_object()

        if not product.file:
            return NotFound(detail='The product has no file')

        response = FileResponse(product.file)
        response['Content-Disposition'] = \
            'attachment; filename=%s' % product.file_name
        response['Content-Length'] = product.file.size

        return response

    filter_fields = ('type', 'name', 'workflowlevel2_uuid', 'part_number', )
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    queryset = Product.objects.all()
    serializer_class = serializer.ProductSerializer
    lookup_field = 'uuid'


class PropertyViewSet(viewsets.ModelViewSet):
    """
    A property is a subset of product that can be allocated to provide
    additional meta descriptions about the product.

    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    def list(self, request):
        # Use this queryset or the django-filters lib will not work
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    filter_fields = ('type', 'product__name', 'name')
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    queryset = Property.objects.all()
    serializer_class = serializer.PropertySerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):

    def list(self, request: Request, *args: Any, **kwargs: Any):
        """
        Return only global OR organization - categories.
        """
        queryset = self.filter_queryset(self.get_queryset())
        if not request.query_params.get('is_global', 'false').lower() == 'true':
            queryset = queryset.filter(organization_uuid=request.session['jwt_organization_uuid'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request: Request, *args: Any, **kwargs: Any):
        """
        Set the `organization_uuid` from the JWT Payload for permission purposes.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organization_uuid=request.session['jwt_organization_uuid'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    filter_fields = ('is_global', )
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    queryset = Category.objects.all()
    serializer_class = serializer.ProductCategorySerializer
    permission_classes = (OrganizationPermission, )
