import random

from faker import Faker

from account.models import UserContact, User
from account.models.user_contact import UserContactDetail

fake = Faker()


def create_user_contact(number_of_contact: int = 100, user: object = None):
    """
    This method create dummy user contact.

    :param number_of_contact: Number of dummy contact(default 100)
    :param user: This parameter used to add user in contact.
    :return: None
    """

    for _ in range(number_of_contact):
        # Here generated only two hundred unique phone number
        # To set same contact number with different name for different user
        phone_number = random.randint(9000000000, 9000000200)

        # Create user contact detail.
        # Here used get_or_create method to create user contact detail
        # because it possible that user contact detail already exists.
        instance, _ = UserContactDetail.objects.get_or_create(
            phone_number=phone_number,
            defaults=dict(email=fake.email())
        )

        # Create user contact as per user contact list name.
        # Here user get_or_create method to avoid the duplication
        # created due to random phone number generator.
        UserContact.objects.get_or_create(
            user=user,
            user_contact_detail=instance,
            defaults=dict(user_name=fake.name())
        )


def create_user():
    """
    This method create dummy user with static values.

    :return: None
    """
    # Create three dummy user
    user_1 = User.objects.create_user(
        user_name=fake.name(),
        password='password@123',
        phone_number=9000000001,
        email=fake.email()
    )

    user_2 = User.objects.create_user(
        user_name=fake.name(),
        password='password@123',
        phone_number=9000000002,
        email=fake.email()
    )

    user_3 = User.objects.create_user(
        user_name=fake.name(),
        password='password@123',
        phone_number=9000000003,
        email=fake.email()
    )

    # Create super admin for admin panel
    super_admin_user = User.objects.create_superuser(
        user_name='admin',
        password='password@123',
        phone_number=11111,
        email=fake.email()
    )

    # Create dummy user contact
    create_user_contact(number_of_contact=50, user=user_1)
    create_user_contact(number_of_contact=100, user=user_2)
    create_user_contact(number_of_contact=30, user=user_3)


create_user()
