from rest_framework.permissions import BasePermission

class Can_create_products(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("users.can_create_product") 

class Can_view_allProducts(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("users.can_view_all_product") 

class Can_view_product(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("users.can_view_products") 