from rest_framework import viewsets, mixins
from rest_framework import permissions
from .serializers import UserDetailSerializer

from .models import UserDetail


class IsOwnerOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        admin can do anything
        if user is not admin, only owner can manipulate data
        """

        # Admin can do anything
        is_admin = request.user.is_superuser
        if is_admin:
            return True

        # Only admin can see the list
        if view.action in ['list']:
            return False

        # Only admin and owner can update and get data
        if view.action in ['retrieve', 'update', 'partial_update']:
            return self.is_owner(request, view=view)

        return False

    def has_object_permission(self, request, view, obj):
        is_admin = request.user.is_superuser
        if is_admin:
            return True
        return self.is_owner(request, obj=obj)

    def is_owner(self, request, **kwargs) -> bool:
        """
        validation to see if the user of request is owner of the data
        """
        user_slug = request.user.slug
        if not isinstance(user_slug, str):
            raise Exception('user_slug is invalid')  # Wrap exception

        if kwargs.get('view', None) is not None:
            obj = kwargs.get('view')
            obj_slug = obj.kwargs.get('slug', None)
            if obj_slug is None:
                raise Exception('Invalid object slug')  # Wrap exception

        if kwargs.get('obj', None) is not None:
            obj = kwargs.get('obj')
            obj_slug = obj.slug
            if not isinstance(obj_slug, str):
                raise Exception('obj_slug is invalid')  # Wrap exception

        is_owner = bool(user_slug == obj_slug)
        return is_owner


class UserDetailUpdateView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    lookup_field = 'slug'
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsOwnerOrAdmin,)

    def partial_update(self, request, *args, **kwargs):
        """
        allow users to update items partially as module name indicates
        """
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

# Another way of updating
# class UserDetailView(viewsets.ModelViewSet):
#     serializer_class = UserDetailSerializer
#     queryset = UserDetail.objects.all()
#     # permission_classes = [IsAccountAdminOrReadOnly]
