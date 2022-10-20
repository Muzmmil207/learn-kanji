from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Character, CharacterExamples, FlashCard
from accounts.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["email", "username", "grade"]


# class CharacterExamplesInline(admin.StackedInline):
#     model = CharacterExamples


# class CharacterAdmin(admin.ModelAdmin):
#     model = Character
#     inlines = [CharacterExamples]
#     fields = ["character"]


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Character, )
admin.site.register(CharacterExamples)
admin.site.register(FlashCard)
