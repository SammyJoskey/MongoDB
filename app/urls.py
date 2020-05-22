from app.views import MessageList, MessageDetail, MessageStat, AddTag, AddComment, AddMessage
from django.urls import path  
from django.views.decorators.cache import cache_page

app_name = 'app'  
urlpatterns = [  
    path('', MessageList.as_view(), name='message_list'),
    path('add/message/', AddMessage.as_view(), name='add_message'),
    path('add/tag/', AddTag.as_view(), name='add_tag'),  
    path('add/comment/', AddComment.as_view(), name='add_comment'),
    path('message/<int:pk>/', MessageDetail.as_view(), name='message_detail'),
    path('stat/<int:pk>/', MessageStat.as_view(), name='message_stat'),
]