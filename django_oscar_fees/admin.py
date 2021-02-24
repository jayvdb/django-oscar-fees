from django.contrib import admin

from .models import Condition, ConditionalFee, Fee, FeeLine, OrderFee

class ConditionalFeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Condition)
admin.site.register(ConditionalFee, ConditionalFeeAdmin)
admin.site.register(Fee)
admin.site.register(FeeLine)
admin.site.register(OrderFee)
