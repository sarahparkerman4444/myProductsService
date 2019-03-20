from django.conf import settings
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated


class AllowOptionsAuthentication(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'OPTIONS':
            return True

        if getattr(request, 'session', None) and \
                request.session.get('jwt_iss') == settings.JWT_ALLOWED_ISSUER:
            return True

        return request.user and request.user.is_authenticated


class OrganizationPermission(AllowOptionsAuthentication):
    def has_permission(self, request, view):
        return super(OrganizationPermission, self).has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if getattr(request, 'session', None):
            if request.session.get('jwt_organization_uuid') == str(obj.organization_uuid):
                return True
            else:
                raise PermissionDenied('User is not in the same organization as the object.')
