from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

from .models import User, Friend, Information, AdjustingEvent
from .forms import FriendFollowForm, ProposeEventForm, AdjustingEventForm
from django.views import generic


class IndexView(generic.ListView):
    model = Information
    template_name = 'index.html'

    def get_queryset(self):
        informations = Information.objects.filter(receiver=self.request.user.id)
        return informations


class ProposeEventView(generic.FormView):
    # NOTE: 一先ずこれ
    template_name = 'propose_event.html'
    form_class = ProposeEventForm
    success_url = reverse_lazy('base:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        friends = [friend.follow_user.id for friend in Friend.objects.filter(followed_user=self.request.user.id)]
        for i in range(1, 4):
            context['form'].fields[f'friend{i}'].queryset = User.objects.filter(id__in=friends)
        return context

    def form_valid(self, form):
        sender = self.request.user
        adjusting_event = form.save(sender)  # データベースに保存するデータ
        friend = adjusting_event.friend1
        info = Information()
        info.receiver = friend
        info.sender = sender
        info.adjusting_event = adjusting_event
        info.save()
        messages.success(self.request, '日程作成に成功しました！')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(self.request.user.id)
        print(form.data)
        print(form.cleaned_data)
        messages.error(self.request, '日程作成に失敗しました...')
        return super().form_invalid(form)


class FriendFollowView(generic.FormView):
    # TODO: 自分自身を対象に友達登録できてしまう
    template_name = 'follow.html'
    form_class = FriendFollowForm
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


class FriendsListView(generic.ListView):
    model = Friend
    template_name = 'friends_list.html'
    paginate_by = 3

    def get_queryset(self):
        friends = Friend.objects.filter(followed_user=self.request.user.id)
        return friends


class AdjustingEventView(generic.FormView):
    template_name = 'adjusting_event.html'
    model = AdjustingEvent
    form_class = AdjustingEventForm
    success_url = reverse_lazy('base:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        adjusting_event = AdjustingEvent.objects.get(pk=pk)
        context['adjusting_event'] = adjusting_event
        return context

    def form_valid(self, form):
        pk = self.kwargs['pk']
        form.update_adjusting_event_table(pk)
        form.save(pk)
        messages.success(self.request, '候補日程を送信しました！')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '候補日程の送信に失敗しました...')
        return super().form_invalid(form)
