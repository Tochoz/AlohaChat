from django.contrib import admin
from .models import PublicChatRoom, PublicChatRoomMessage, Message
# Register your models here.
admin.site.register(PublicChatRoomMessage)
admin.site.register(PublicChatRoom)
admin.site.register(Message)

