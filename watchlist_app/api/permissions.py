from rest_framework import permissions

class AdminOrReadonly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        user_check = request.user
        print(user_check)
        print(request.user.is_staff)
        print(request.user and request.user.is_staff)
        admin_permission =  bool(request.user and request.user.is_staff)
        print(admin_permission)
        return request.method == "GET" or admin_permission
    
    # def has_permission(self, request, view):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     else:
    #         return bool(request.user and request.user.is_staff)
        


class ReviewUserOrReadonly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
        # Check permissions for read-only request
            return True
        else:
        # Check permissions for write request
            return obj.review_user == request.user

