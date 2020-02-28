from rest_framework import viewsets, mixins
from rest_framework import permissions
from .serializers import UserDetailSerializer

from .models import UserDetail


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        is_admin = request.user.is_superuser
        if is_admin:
            return True
        return bool(obj.user == request.user)


class UserDetailUpdateView(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = UserDetail.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsOwner,)

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
