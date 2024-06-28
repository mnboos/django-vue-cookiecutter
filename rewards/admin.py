from django.contrib import admin

from rewards.models import Reward


class RewardAdmin(admin.ModelAdmin):
    list_display = ['name', 'point_value']
    list_filter = ['point_value']
    search_fields = ['name']


admin.site.register(Reward, RewardAdmin)
