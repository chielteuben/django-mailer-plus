from django.contrib import admin
from django_mailer_plus import models


class Message(admin.ModelAdmin):
    list_display = ('to_address', 'subject', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('to_address', 'subject', 'from_address', 'encoded_message',)
    date_hierarchy = 'date_created'
    ordering = ('-date_created',)


class MessageRelatedModelAdmin(admin.ModelAdmin):
    list_select_related = True

    def message__to_address(self, obj):
        return obj.message.to_address
    message__to_address.admin_order_field = 'message__to_address'

    def message__subject(self, obj):
        return obj.message.subject
    message__subject.admin_order_field = 'message__subject'

    def message__date_created(self, obj):
        return obj.message.to_address
    message__date_created.admin_order_field = 'message__date_created'


class QueuedMessage(MessageRelatedModelAdmin):
    def not_deferred(self, obj):
        return not obj.deferred
    not_deferred.boolean = True
    not_deferred.admin_order_field = 'deferred'

    list_display = ('id', 'message__to_address', 'message__subject',
                    'message__date_created', 'priority', 'not_deferred')


class Blacklist(admin.ModelAdmin):
    list_display = ('email', 'date_added')


class Log(MessageRelatedModelAdmin):
    list_display = ('id', 'result', 'message__to_address', 'message__subject',
                    'date')
    list_filter = ('result',)
    list_display_links = ('id', 'result')
    search_fields = ('id', 'message__to_address', 'message__subject')


admin.site.register(models.Message, Message)
admin.site.register(models.QueuedMessage, QueuedMessage)
admin.site.register(models.Blacklist, Blacklist)
admin.site.register(models.Log, Log)
