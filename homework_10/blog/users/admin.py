from django.contrib import admin

from users.models import User, Friend

# Register your models here.

admin.site.register(User)
admin.site.register(Friend)
# admin.site.register(UserFriend)
