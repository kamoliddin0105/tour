from rest_framework import permissions


class IsReviewOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff == obj.user or request.user