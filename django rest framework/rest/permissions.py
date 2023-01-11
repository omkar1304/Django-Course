from rest_framework.permissions import DjangoModelPermissions, BasePermission

class CustomDjangoModelPermissions(DjangoModelPermissions):

    # format -> appname.action_modelname | for example -> rest.view_product
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'], # here we added in get method that user can view product who has access
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # we can use like this or just add IsAdminUser in permission_classes in views 
    # permission_classes = [permissions.IsAdminUser,CustomDjangoModelPermissions]
    '''def has_permission(self, request, view):
        user = request.user
        if not user.is_staff: # here we are actually implementing IsAdminUser permission 
            return False
        return super().has_permission(request, view)'''


    # this method only to understand how we can assign permission based views to user
    '''def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            # format -> appname.action_modelname | for example -> rest.view_product
            if user.has_perm('rest.view_product'): 
                return True
            if user.has_perm('rest.change_product'):
                return True
            if user.has_perm('rest.add_product'):
                return True
            if user.has_perm('rest.delete_product'):
                return True
            return False
        return False'''


class CustomPermissions(BasePermission):
    # this is how we can overried below two methods and create custom permissions
    
    def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            # format -> appname.action_modelname | for example -> rest.view_product
            if user.has_perm('rest.view_product'): 
                return True
            if user.has_perm('rest.change_product'):
                return True
            if user.has_perm('rest.add_product'):
                return True
            if user.has_perm('rest.delete_product'):
                return True
            return False
        return False

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)