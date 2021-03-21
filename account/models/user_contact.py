from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from ContactInformation.models import BaseModel

__all__ = ['UserContact', 'UserContactDetail']

from account.models import User


class UserContact(BaseModel):
    """
    Created this class to store user's contact.
    """
    user_name = models.CharField(max_length=30)
    user_contact_detail = models.ForeignKey('account.UserContactDetail',
                                            on_delete=models.CASCADE)
    user = models.ForeignKey('account.User', blank=True, null=True,
                             on_delete=models.SET_NULL)


class UserContactDetail(BaseModel):
    """
    Created this class to store user's contact detail.
    """
    phone_number = models.PositiveBigIntegerField(unique=True)
    email = models.EmailField(blank=True, null=True)
    is_spam = models.BooleanField(default=False)
    users = models.ManyToManyField('account.user',
                                   through='account.UserContact')


@receiver(post_save, sender=User)
def create_user_contact(sender, instance, **kwargs):
    """
    This method create user contact record on register of user.

    :param sender: User model
    :param instance: user model record
    :param kwargs: extra arguments
    :return: None
    """
    # Create user contact detail.
    # Here used get_or_create method to create user contact detail
    # because it possible that user contact detail already exists.
    user_contact_detail, _ = UserContactDetail.objects.get_or_create(
        phone_number=instance.phone_number,
        defaults=dict(email=instance.email)
    )

    # Create user contact as per user contact list name.
    UserContact.objects.create(user_name=instance.user_name, user=instance,
                               user_contact_detail=user_contact_detail)
