from rest_framework import serializers

from account.models import UserContact

__all__ = ['UserContactSerializer']


class UserContactSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    phone_number = serializers.CharField(
        source='user_contact_detail.phone_number'
    )
    is_spam = serializers.CharField(source='user_contact_detail.is_spam')

    class Meta:
        model = UserContact
        fields = ['id', 'user_name', 'phone_number', 'email', 'is_spam']

    def get_email(self, instance):
        """
        This method check login user based on that it return email value.

        :param instance: UserContact record
        :return: email or blank string
        """
        email = ''
        # Get view request to get login user.
        if request := self.context.get('request'):
            email = request.user in instance.user_contact_detail.users.all() \
                    and instance.user_contact_detail.email or ''
        return email
