from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read only permission are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permission are only allowed to the author of a post
        return obj.author == request.user


class IsSelfOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read only permission are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permission are only allowed to the author of a post
        return obj.username == request.user
