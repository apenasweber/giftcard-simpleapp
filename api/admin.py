from django.contrib import admin

from .models import GiftCardLogs, GiftCards


class GiftCardLogsInline(admin.TabularInline):
    readonly_fields = ("date_time", "used_amount", "order_number")
    model = GiftCardLogs
    extra = 0


class GiftCardsAdmin(admin.ModelAdmin):
    inlines = [GiftCardLogsInline]


admin.site.register(GiftCards, GiftCardsAdmin)
admin.site.register(GiftCardLogs)
