from django.contrib import admin
from .models import Quote, Mission, SideImage
from .models import TeamMember
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("text",)


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(SideImage)
class SideImageAdmin(admin.ModelAdmin):
    list_display = ("position", "image")
    list_filter = ("position",)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "blood_group", "mobile", "email")