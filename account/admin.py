from django.contrib import admin

from account.models import User, UserContact, UserContactDetail


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'phone_number', 'email')


class UserContactInline(admin.TabularInline):
    model = UserContact
    max_num = 0


@admin.register(UserContactDetail)
class UserContactDetailAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'is_spam', 'get_users')
    inlines = [UserContactInline]

    def get_users(self, instance):
        """
        Created this method to display user name in user contact detail list.

        :param instance: USer contact detail record
        :return: string
        """
        return ", ".join([user.user_name for user in instance.users.all()])
