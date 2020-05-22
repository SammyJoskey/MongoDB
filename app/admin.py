from django.contrib import admin
from app.models import Message, Tag, Comment

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body']
    fields = ['title', 'body', 'tags']

class CommentAdmin(admin.ModelAdmin):
    fields = ['title', 'message']

class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    fields = ['title']


admin.site.register(Message, MessageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)