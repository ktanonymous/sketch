from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms
from allauth.account.forms import SignupForm

from .models import AdjustingEvent, Event, Friend, Information, User

# 日付入力欄をカレンダー形式にするために設定
DATETIME_WIDGET = DateTimePickerInput(
    format='%Y-%m-%d %H:%M',
    options={'locale': 'ja', 'dayViewHeaderFormat': 'YYYY年 MMMM'}
)


class FriendFollowForm(forms.Form):
    # 誰にも申請を送らないという状況にならないようにするため、1つ目のメアドは必須にしている
    email1 = forms.EmailField(max_length=255, label='Email1')
    email2 = forms.EmailField(max_length=255, label='Email2', required=False)
    email3 = forms.EmailField(max_length=255, label='Email3', required=False)
    email4 = forms.EmailField(max_length=255, label='Email4', required=False)
    email5 = forms.EmailField(max_length=255, label='Email5', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in range(1, 6):
            self.fields[f"email{i}"].widget.attrs['class'] = 'form-control'
            self.fields[f"email{i}"].widget.attrs['placeholder'] = 'example@example.com'

    def save(self, applicant):
        data = self.cleaned_data
        emails = [email for email in data.values() if email]
        users = [User.objects.get(email=email) for email in emails]
        # TODO: 現状、A が B に申請すると A<-->B の関係になるが、A-->B の関係にしたい
        for user in users:
            Friend(follow_user=applicant, followed_user=user).save()
            Friend(follow_user=user, followed_user=applicant).save()


class ProposeEventForm(forms.ModelForm):
    class Meta:
        model = AdjustingEvent
        fields = (
            'name',
            'date1_start', 'date1_end',
            'date2_start', 'date2_end',
            'date3_start', 'date3_end',
            'date4_start', 'date4_end',
            'date5_start', 'date5_end',
            'friend1', 'friend2', 'friend3'
        )
        # 各日程の開始時間と終了時間をカレンダーで入力できるようにする
        # ModelForm を継承しているため、Meta クラスで widget を定義する
        widgets = {
            f"date{i}_{suffix}": DATETIME_WIDGET
            for i in range(1, 6)
            for suffix in ('start', 'end')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in range(1, 6):
            self.fields[f"date{i}_start"].widget.attrs['class'] = 'form-control'
            self.fields[f"date{i}_end"].widget.attrs['class'] = 'form-control'

        for i in range(1, 4):
            self.fields[f"friend{i}"].widget.attrs['class'] = 'form-control'

    def save(self, proposer):
        cleaned_data = self.cleaned_data

        adjusting_event = AdjustingEvent(**cleaned_data)
        adjusting_event.proposer = proposer

        # 日程調整をしていない友達の残り人数を更新する
        friends = [adjusting_event.friend1, adjusting_event.friend2, adjusting_event.friend3]
        adjusting_event.rest_friends_num = sum(friend is not None for friend in friends)

        adjusting_event.save()
        return adjusting_event


class AdjustingEventForm(forms.Form):
    date1_is_ok = forms.BooleanField(
        initial=False, required=False, label='日程1', widget=forms.CheckboxInput()
    )
    date2_is_ok = forms.BooleanField(
        initial=False, required=False, label='日程2', widget=forms.CheckboxInput()
    )
    date3_is_ok = forms.BooleanField(
        initial=False, required=False, label='日程3', widget=forms.CheckboxInput()
    )
    date4_is_ok = forms.BooleanField(
        initial=False, required=False, label='日程4', widget=forms.CheckboxInput()
    )
    date5_is_ok = forms.BooleanField(
        initial=False, required=False, label='日程5', widget=forms.CheckboxInput()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(1, 6):
            self.fields[f"date{i}_is_ok"].widget.attrs['class'] = 'form-control'

    def update_adjusting_event_table(self, pk):
        # TODO: 調整中に日程候補が全部拒否された場合の動作が実装されていない
        cleaned_data = self.cleaned_data
        adjusting_event = AdjustingEvent.objects.get(pk=pk)
        adjusting_event.rest_friends_num -= 1

        for i in range(1, 6):
            if not cleaned_data[f"date{i}_is_ok"]:
                setattr(adjusting_event, f"date{i}_start", None)
                setattr(adjusting_event, f"date{i}_end", None)

        adjusting_event.save()

    def save(self, pk):
        adjusting_event = AdjustingEvent.objects.get(pk=pk)
        event_name = adjusting_event.name
        rest_friends_num = adjusting_event.rest_friends_num
        sender = adjusting_event.proposer
        friends = [adjusting_event.friend1, adjusting_event.friend2, adjusting_event.friend3]
        friends = [friend for friend in friends if friend]
        old_information = Information.objects.get(adjusting_event=pk)

        if rest_friends_num == 0:
            # 日程調整が完了しているため、イベント情報を登録して「調整中」から除外する
            self._save_event(event_name, adjusting_event, friends, sender)
            adjusting_event.delete()
        else:
            # 次の依頼先にイベント情報を送信する
            next_friend_index = len(friends) - rest_friends_num + 1
            next_friend = getattr(adjusting_event, f"friend{next_friend_index}")

            information = Information()
            information.event_name = event_name
            information.sender = sender
            receiver = next_friend
            information.receiver = receiver
            information.adjusting_event = adjusting_event
            information.save()

        old_information.delete()

    def _save_event(self, event_name, adjusting_event, friends, sender):
        # 確定したイベント日時を調べる
        for i in range(1, 6):
            date_start = getattr(adjusting_event, f"date{i}_start")
            date_end = getattr(adjusting_event, f"date{i}_end")
            if date_start is not None:
                break

        # 参加者ごとにイベントの詳細とお知らせを登録する
        participants = friends + [sender]
        for participant in participants:
            event = Event()
            event.name = event_name
            event.date_start = date_start
            event.date_end = date_end
            event.participant = participant
            event.save()

            information = Information()
            information.event_name = event_name
            information.receiver = participant
            information.sender = sender
            information.event = event
            information.save()

class MyCustomSignupForm(SignupForm):
    field_order = ['username', 'email', 'password'] #formのfieldの表示順序を変更.BaseSignupFormのコンストラクタのset_form_field_orderで用いる.

