from rest_framework import viewsets
from .serializers import UserDetailSerializer
from .models import UserDetail


class UserDetailView(viewsets.ModelViewSet):
    serializer_class = UserDetailSerializer
    queryset = UserDetail.objects.all()
