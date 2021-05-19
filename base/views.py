from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

from .models import User, Friend, Event, Information, AdjustingSchedule
from .forms import FriendFollowForm, AdjustingScheduleForm
from django.views import generic


class IndexView(generic.ListView):
    model = Information
    template_name = 'index.html'

    def get_queryset(self):
        informations = Information.objects.filter(user_id=self.request.user.id)
        return informations


class AdjustingScheduleView(generic.FormView):
    # NOTE: 一先ずこれ
    template_name = 'adjusting_schedule.html'
    form_class = AdjustingScheduleForm
    success_url = reverse_lazy('base:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: 明らかにfollow_user_id.idはおかしいので要検討
        friend_ids = [friend.follow_user_id.id for friend in Friend.objects.filter(followed_user_id=self.request.user.id)]
        for i in range(1, 4):
            context['form'].fields[f'friend{i}'].queryset = User.objects.filter(id__in=friend_ids)
        return context

    def form_valid(self, form):
        print('success!')
        print(form.data)
        print(form.cleaned_data)
        messages.success(self.request, '日程作成に成功しました！')
        return super().form_valid(form)

    def form_invalid(self, form):
        print('failed...')
        print(self.request.user.id)
        print(form.data)
        print(form.cleaned_data)
        messages.error(self.request, '日程作成に失敗しました...')
        return super().form_invalid(form)


class FriendFollowView(generic.FormView):
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
        friends = Friend.objects.filter(followed_user_id=self.request.user.id)
        return friends
