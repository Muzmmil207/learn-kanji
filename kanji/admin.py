from accounts.models import User
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Character, CharacterExamples, FlashCard

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["email", "username", "grade"]


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(
    Character,
)
admin.site.register(CharacterExamples)
admin.site.register(FlashCard)
