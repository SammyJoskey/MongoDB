from app.models import Message, Tag, Comment
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):

    # comments = CommentSerializer() 


    class Meta:  
        model = Message  
        fields = ['id', 'title', 'body', 'date_adv', 'tags']

class CommentSerializer(serializers.ModelSerializer):

    class Meta:  
        model = Comment  
        fields = ['title', ]


class TagSerializer(serializers.ModelSerializer):

    class Meta:  
        model = Tag  
        fields = '__all__'