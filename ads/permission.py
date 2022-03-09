from django.http import Http404
from rest_framework import permissions

from ads.models import User, Ad, Selection


class SelectionUpdatePermission(permissions.BasePermission):
    message = 'Managing others selections not permitted.'

    def has_permission(self, request, view):
        entity = Selection.objects.get(pk=view.kwargs["pk"])
        if entity.owner_id == request.user.id:
            return True
        return False


class AdUpdatePermission(permissions.BasePermission):
    message = 'Managing others ads not permitted.'

    def has_permission(self, request, view):
        if request.user.role in [User.MEMBER, User.ADMIN]:
            return True
        entity = Ad.objects.get(pk=view.kwargs["pk"])
        if entity.author_id == request.user.id:
            return True
        return False


