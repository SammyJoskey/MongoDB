from django.forms import ModelForm
from app.models import Message, Tag, Comment


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'body' )

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ('title', 'mess')

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'message')

