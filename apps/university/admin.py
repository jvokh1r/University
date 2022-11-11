from django.contrib import admin
from .models import FAQ, Service, Reason


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', )
    list_filter = ('id', 'question')
    search_fields = ['question', ]
    search_help_text = 'search here'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', )
    list_filter = ('id', 'service_title')
    search_fields = ['service_filter', ]
    search_help_text = 'search here'


class ReasonAdmin(admin.ModelAdmin):
    list_display = ('reason_title', )
    list_filter = ('id', 'reason_title')
    search_fields = ['reason_title', ]
    search_help_text = 'search here'


admin.site.register(FAQ, FaqAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Reason, ReasonAdmin)
