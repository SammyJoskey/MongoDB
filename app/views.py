from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import ListView, View, DetailView, CreateView, UpdateView
from django.views.generic.edit import BaseUpdateView
from django.urls import reverse_lazy
import redis
import pickle

from app.models import Message, Tag, Comment
from app.forms import MessageForm, TagForm, CommentForm

cache = redis.Redis(host='127.0.0.1', port=6379)

class AddMessage(CreateView):
    template_name = 'add_message.html'
    form_class = MessageForm
    success_url = reverse_lazy('app:message_list')

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            message.save()
            messages = Message.objects.all()
            cache.set('messages', pickle.dumps(messages))
            return HttpResponseRedirect(reverse_lazy('app:message_list'))
        return HttpResponseRedirect(reverse_lazy('app:message_list'))

class AddTag(CreateView):
    template_name = 'add_tag.html'
    form_class = TagForm
    success_url = reverse_lazy('app:message_list')
    
class AddComment(CreateView):
    template_name = 'add_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('app:message_list')

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.save()
            messages = Message.objects.all()
            cache.set('messages', pickle.dumps(messages))
            return HttpResponseRedirect(reverse_lazy('app:message_list'))
        return HttpResponseRedirect(reverse_lazy('app:message_list'))


class MessageList(ListView):
    model = Message
    template_name = 'message_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages = cache.get('messages')
        if messages:
            messages_value = pickle.loads(messages)
        else:
            messages_value = Message.objects.all()
            cache.set('messages', pickle.dumps(messages_value))
        context['message_list'] = messages_value
        return context

class MessageDetail(DetailView):
    model = Message
    template_name = 'message_detail.html'
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages = cache.get('messages')
        if messages:
            messages_value = pickle.loads(messages)
        else:
            messages_value = Message.objects.all()
            cache.set('messages', pickle.dumps(messages_value))
        context['message'] = messages_value.get(pk=self.kwargs['pk'])
        return context
        
class MessageStat(DetailView):
    model = Message
    template_name = 'message_stat.html'
    context_object_name = 'message'

