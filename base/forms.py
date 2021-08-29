"""
フォームの詳細を設定する
"""

import sys

from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput
from .models import User, Friend, AdjustingEvent, Information, Event

datetime_widget = DateTimePickerInput(
    format='%Y-%m-%d %H:%M',
    options={'locale': 'ja', 'dayViewHeaderFormat': 'YYYY年 MMMM'}
)


class FriendFollowForm(forms.Form):
    email1 = forms.EmailField(max_length=255, label='Email1',)
    email2 = forms.EmailField(max_length=255, label='Email2', required=False)
    email3 = forms.EmailField(max_length=255, label='Email3', required=False)
    email4 = forms.EmailField(max_length=255, label='Email4', required=False)
    email5 = forms.EmailField(max_length=255, label='Email5', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email1'].widget.attrs['class'] = 'form-control'
        self.fields['email2'].widget.attrs['class'] = 'form-control'
        self.fields['email3'].widget.attrs['class'] = 'form-control'
        self.fields['email4'].widget.attrs['class'] = 'form-control'
        self.fields['email5'].widget.attrs['class'] = 'form-control'

        self.fields['email1'].widget.attrs['placeholder'] = 'example@example.com'
        self.fields['email2'].widget.attrs['placeholder'] = 'example@example.com'
        self.fields['email3'].widget.attrs['placeholder'] = 'example@example.com'
        self.fields['email4'].widget.attrs['placeholder'] = 'example@example.com'
        self.fields['email5'].widget.attrs['placeholder'] = 'example@example.com'

    def save(self, self_user):
        data = self.cleaned_data
        emails = [email for email in data.values() if email]
        users = [User.objects.get(email=email) for email in emails]
        for user in users:
            Friend(follow_user=self_user, followed_user=user).save()
            Friend(follow_user=user, followed_user=self_user).save()


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
        widgets = {
            f"date{i}_{j}": datetime_widget
            for i in range(1, 6)
            for j in ('start', 'end')
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
        adjusting_event = AdjustingEvent()
        adjusting_event.proposer = proposer
        adjusting_event.name = cleaned_data['name']
        adjusting_event.date1_start = cleaned_data['date1_start']
        adjusting_event.date1_end = cleaned_data['date1_end']
        adjusting_event.date2_start = cleaned_data['date2_start']
        adjusting_event.date2_end = cleaned_data['date2_end']
        adjusting_event.date3_start = cleaned_data['date3_start']
        adjusting_event.date3_end = cleaned_data['date3_end']
        adjusting_event.date4_start = cleaned_data['date4_start']
        adjusting_event.date4_end = cleaned_data['date4_end']
        adjusting_event.date5_start = cleaned_data['date5_start']
        adjusting_event.date5_end = cleaned_data['date5_end']
        adjusting_event.friend1 = cleaned_data['friend1']
        adjusting_event.friend2 = cleaned_data['friend2']
        adjusting_event.friend3 = cleaned_data['friend3']

        friends = [adjusting_event.friend1, adjusting_event.friend2, adjusting_event.friend3]
        adjusting_event.rest_friends_num = sum(friend is not None for friend in friends)
        adjusting_event.save()
        return adjusting_event


class AdjustingEventForm(forms.Form):
    date1_is_ok = forms.BooleanField(initial=False, required=False, label='日程1', widget=forms.CheckboxInput())
    date2_is_ok = forms.BooleanField(initial=False, required=False, label='日程2', widget=forms.CheckboxInput())
    date3_is_ok = forms.BooleanField(initial=False, required=False, label='日程3', widget=forms.CheckboxInput())
    date4_is_ok = forms.BooleanField(initial=False, required=False, label='日程4', widget=forms.CheckboxInput())
    date5_is_ok = forms.BooleanField(initial=False, required=False, label='日程5', widget=forms.CheckboxInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(1, 6):
            self.fields[f"date{i}_is_ok"].widget.attrs['class'] = 'form-control'

    def update_adjusting_event_table(self, pk):
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
        friends = [getattr(adjusting_event, f"friend{i}") for i in range(1, 4)]
        friends = [friend for friend in friends if friend]
        # TODO: 日程候補が全部なくなった場合も実装したい
        # TODO: セーブする前に削除されるのはいかがなものか
        old_information = Information.objects.get(adjusting_event=pk)

        if rest_friends_num == 0:
            self._save_event(event_name, adjusting_event, friends, sender)
            adjusting_event.delete()
        else:
            friend_number = len(friends) - rest_friends_num + 1
            next_friend = getattr(adjusting_event, f"friend{friend_number}")
            information = Information()
            information.event_name = event_name
            information.sender = sender
            receiver = next_friend
            information.receiver = receiver
            information.adjusting_event = adjusting_event
            information.save()

        old_information.delete()

    def _save_event(self, event_name, adjusting_event, friends, sender):
        for i in range(1, 6):
            date_start = getattr(adjusting_event, f"date{i}_start")
            date_end = getattr(adjusting_event, f"date{i}_end")
            if date_start is not None:
                break
        participants = friends + [sender]
        for participant in participants:
            event = Event()
            information = Information()

            event.name = event_name
            event.date_start = date_start
            event.date_end = date_end
            event.participant = participant

            information.event_name = event_name
            information.receiver = participant
            information.sender = sender
            information.event = event

            event.save()
            information.save()
