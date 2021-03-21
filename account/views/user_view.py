from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import User
from account.serializers import UserSerializer

__all__ = ['UserViewSet']


class UserViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    model = User
    queryset = model.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['phone_number']
    search_fields = ['user_name', 'phone_number']
    http_method_names = ['post', 'patch']

    @action(detail=False, methods=['post'], permission_classes=[])
    def register(self, request: object) -> object:
        """
        This API provide functionality to register user.

        :param request: View request object.
        :return: User detail
        """
        # Validate user data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create User
        User.objects.create_user(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
