
from rest_framework import permissions

from ads.models import User, Selection


class SelectionUpdatePermission(permissions.BasePermission):
    message = 'Managing others selections not permitted.'

    def has_permission(self, request, view):
        entity = Selection.objects.get(pk=view.kwargs["pk"])
        if entity.owner_id == request.user.id:
            return True
        return False

class IsAuthenticatedAndOwner(permissions.BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class AdUpdatePermission(permissions.BasePermission):
    message = 'Managing others ads not permitted.'

    def has_permission(self, request, view):
        if request.user.role in [User.MEMBER, User.ADMIN]:
            return True
        return False




