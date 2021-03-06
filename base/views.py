import json
import datetime

from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import AdjustingEventForm, FriendFollowForm, ProposeEventForm
from .models import AdjustingEvent, Friend, Information, User


class IndexView(generic.ListView):
    model = Information
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        informations = self.get_queryset()
        DIFF_JST_FROM_UTC = 9
        DIFF = datetime.timedelta(hours=DIFF_JST_FROM_UTC)
        TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
        informations_dict = {
            information.event_name: {
                'start': (information.event.date_start + DIFF).strftime(TIME_FORMAT),
                'end': (information.event.date_end + DIFF).strftime(TIME_FORMAT),
            }
            for information in informations
            if information.event
        }

        context['informations_data'] = json.dumps(informations_dict)
        return context

    def get_queryset(self):
        informations = Information.objects.filter(receiver=self.request.user.id)
        return informations


class ProposeEventView(generic.FormView):
    template_name = 'propose_event.html'
    form_class = ProposeEventForm
    success_url = reverse_lazy('base:index')

    def get_context_data(self, **kwargs):
        """テンプレートに渡すデータに招待できる友人のリスト情報を追加する"""
        # テンプレートに渡す情報を取得する
        context = super().get_context_data(**kwargs)

        # Friend テーブルから、利用ユーザーの友達のリストを取得する
        user_id = self.request.user.id
        friends = Friend.objects.filter(followed_user=user_id)
        friend_ids = [friend.follow_user.id for friend in friends]
        friends_list = User.objects.filter(id__in=friend_ids)

        # イベントに招待する人の選択肢として、利用ユーザーの友達リストをテンプレートに渡す
        # TODO: この実装のままだと、同じ友達を複数回選ぶことができてしまう
        for i in range(1, 4):
            context['form'].fields[f'friend{i}'].queryset = friends_list

        return context

    def form_valid(self, form):
        # 1人目の友達に情報を送るために新しく作成された調整中のイベントを取得する
        adjusting_event = form.save(proposer=self.request.user)

        info = Information()
        # 最初は、1人目の友達に調整依頼を送る
        info.receiver = adjusting_event.friend1
        info.sender = self.request.user
        info.adjusting_event = adjusting_event
        info.save()

        messages.success(self.request, '日程作成に成功しました！')

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '日程作成に失敗しました...')
        return super().form_invalid(form)


class FriendFollowView(generic.FormView):
    # TODO: 自分自身を対象に友達登録できてしまう
    template_name = 'follow.html'
    form_class = FriendFollowForm
    model = Friend
    success_url = reverse_lazy('base:index')

    def form_valid(self, form):
        form.save(applicant=self.request.user)
        messages.success(self.request, '友達登録が完了致しました！')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '友達登録に失敗しました...')
        return super().form_invalid(form)


class FriendsListView(generic.ListView):
    model = Friend
    template_name = 'friends_list.html'
    paginate_by = 20

    def get_queryset(self):
        friends = Friend.objects.filter(followed_user=self.request.user.id)
        return friends


class AdjustingEventView(generic.FormView):
    template_name = 'adjusting_event.html'
    model = AdjustingEvent
    form_class = AdjustingEventForm
    success_url = reverse_lazy('base:index')

    def get_context_data(self, **kwargs):
        """テンプレートに渡す所望の日程調整中イベントを追加する"""
        context = super().get_context_data(**kwargs)

        pk = self.kwargs['pk']
        adjusting_event = AdjustingEvent.objects.get(pk=pk)

        TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
        DIFF_JST_FROM_UTC = 9
        DIFF = datetime.timedelta(hours=DIFF_JST_FROM_UTC)
        data = {
            'title': adjusting_event.name,
            'date1_start': (adjusting_event.date1_start + DIFF).strftime(TIME_FORMAT) if adjusting_event.date1_start else None,
            'date1_end': (adjusting_event.date1_end + DIFF).strftime(TIME_FORMAT) if adjusting_event.date1_end else None,
            'date2_start': (adjusting_event.date2_start + DIFF).strftime(TIME_FORMAT) if adjusting_event.date2_start else None,
            'date2_end': (adjusting_event.date2_end + DIFF).strftime(TIME_FORMAT) if adjusting_event.date2_end else None,
            'date3_start': (adjusting_event.date3_start + DIFF).strftime(TIME_FORMAT) if adjusting_event.date3_start else None,
            'date3_end': (adjusting_event.date3_end + DIFF).strftime(TIME_FORMAT) if adjusting_event.date3_end else None,
            'date4_start': (adjusting_event.date4_start + DIFF).strftime(TIME_FORMAT) if adjusting_event.date4_start else None,
            'date4_end': (adjusting_event.date4_end + DIFF).strftime(TIME_FORMAT) if adjusting_event.date4_end else None,
            'date5_start': (adjusting_event.date5_start + DIFF).strftime(TIME_FORMAT) if adjusting_event.date5_start else None,
            'date5_end': (adjusting_event.date5_end + DIFF).strftime(TIME_FORMAT) if adjusting_event.date5_end else None,
        }
        context['data_json'] = json.dumps(data)
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
