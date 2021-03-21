from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import UserContact
from account.serializers import UserContactSerializer

__all__ = ['UserContactViewSet']


class UserContactViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    model = UserContact
    queryset = model.objects.all()
    serializer_class = UserContactSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['user_name', 'user_contact_detail__phone_number']
    http_method_names = ['get']

    @action(detail=True)
    def spam(self, request, pk, *args, **kwargs):
        """
        This API provide functionality set user contact as spam.

        :param request: View request objects.
        :param pk: User contact record id.
        :param args: List of position argument.
        :param kwargs: Dictionary contain method keyword argument.
        :return:
        """
        # Set spam flag as true
        user_contact = self.get_object()
        user_contact.user_contact_detail.is_spam = True
        user_contact.user_contact_detail.save()

        # Get json data using serializer
        serializer = self.get_serializer(user_contact)

        return Response(serializer.data, status=status.HTTP_200_OK)
