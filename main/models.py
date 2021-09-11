from django.db import models
from django.conf import settings

class Name(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Message(models.Model):
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(unique=False, blank=False)

class PublicChatRoom(models.Model):
    title = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, help_text="connected users")

    def __str__(self):
        return self.title

    def connect_user(self, user):
        """
        return True if success
        """
        success = False

        if not user in self.users.all():
            self.users.add(user)
            self.users.save()
            success = True
        elif user in self.users.all():
            success = True
        return success

    def disconnect_user(self, user):
        success = False

        if user in self.users.all():
            self.users.delete(user)
            self.users.save()
            success = True
        return success

    @property
    def group_name(self):
        """Returns channel group for sockets subscribition"""
        return f"PublicChatRoom-{self.id}"

class PublicChatRoomMessageManager(models.Manager):
    def by_room(self, room):
        qs = PublicChatRoomMessage.objects.filter(room=room).order_by("-timestamp")
        return qs

class PublicChatRoomMessage(models.Model):

    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room        = models.ForeignKey(PublicChatRoom, on_delete=models.CASCADE)
    timestamp   = models.DateTimeField(auto_now_add=True)
    content     = models.TextField(unique=False, blank=False)

    objects = PublicChatRoomMessageManager()

    def __str__(self):
        return self.content
