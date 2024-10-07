from django.contrib import admin
from .models import Conversation

# Define admin display for Conversation model
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'message_excerpt', 'response_excerpt', 'timestamp')
    search_fields = ('user_id', 'message', 'response')
    list_filter = ('timestamp',)
    readonly_fields = ('user_id', 'message', 'response', 'timestamp')

    # Show only a part of the message and response for brevity
    def message_excerpt(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_excerpt.short_description = 'Message'

    def response_excerpt(self, obj):
        return obj.response[:50] + '...' if len(obj.response) > 50 else obj.response
    response_excerpt.short_description = 'Response'