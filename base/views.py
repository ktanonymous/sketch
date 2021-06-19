from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

from .models import User, Friend, Information, AdjustingSchedule
from .forms import FriendFollowForm, ProposeScheduleForm, AdjustingScheduleForm
from django.views import generic


class IndexView(generic.ListView):
    model = Information
    template_name = 'index.html'

    def get_queryset(self):
        informations = Information.objects.filter(receiver=self.request.user.id)
        return informations


class ProposeScheduleView(generic.FormView):
    # NOTE: 一先ずこれ
    template_name = 'propose_schedule.html'
    form_class = ProposeScheduleForm
    success_url = reverse_lazy('base:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        friends = [friend.follow_user.id for friend in Friend.objects.filter(followed_user=self.request.user.id)]
        for i in range(1, 4):
            context['form'].fields[f'friend{i}'].queryset = User.objects.filter(id__in=friends)
        return context

    def form_valid(self, form):
        sender = self.request.user
        adjusting_schedule = form.save(sender)  # データベースに保存するデータ
        friend = adjusting_schedule.friend1
        info = Information()
        info.receiver = friend
        info.sender = sender
        info.adjusting_schedule = adjusting_schedule
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


class AdjustingScheduleView(generic.FormView):
    template_name = 'adjusting_schedule.html'
    model = AdjustingSchedule
    form_class = AdjustingScheduleForm
    success_url = reverse_lazy('base:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        adjusting_schedule = AdjustingSchedule.objects.get(pk=pk)
        context['adjusting_schedule'] = adjusting_schedule
        return context

    def form_valid(self, form):
        pk = self.kwargs['pk']
        form.update_adjusting_schedule_table(pk)
        form.save(pk)
        messages.success(self.request, '候補日程を送信しました！')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '候補日程の送信に失敗しました...')
        return super().form_invalid(form)
