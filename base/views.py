from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

from .models import User, Friend, Event, Information, AdjustingSchedule
from .forms import FriendApplicationForm
from django.views import generic


class IndexView(generic.ListView):
    model = Information
    template_name = 'index.html'

    def get_queryset(self):
        informations = Information.objects.filter(user_id=self.request.user.id)
        return informations


class FriendsListView(generic.ListView):
    model = Friend
    template_name = 'friends_list.html'
    paginate_by = 3

    def get_queryset(self):
        friends = Friend.objects.filter(followed_user_id=self.request.user.id)
        return friends


class FriendApplicationView(generic.FormView):
    template_name = 'friend_application.html'
    form_class = FriendApplicationForm
    model = Friend
    success_url = reverse_lazy('base:index')

    def form_valid(self, form):
        self_user = self.request.user
        form.save(self_user)
        messages.success(self.request, '友達登録が完了致しました！')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '友達登録に失敗しました...')
        return super().form_invalid(form)
