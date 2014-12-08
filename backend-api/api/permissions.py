from rest_framework import permissions


class InstitutionDetailPermissionsTest(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # obj is the actual model instance (as in, an actual institution)
        # obj is return by a method called get_object() on the actual view
        # request.user returns the id of the user currently logged in

        # SAFE = GET, HEAD and OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # for testing purposes, only allow POST if institution.id = 1
        return obj.id == 1