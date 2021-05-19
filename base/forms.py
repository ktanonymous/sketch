import sys

from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput
from .models import User, Friend, Information, AdjustingSchedule

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
            Friend(follow_user_id=self_user, followed_user_id=user).save()
            Friend(follow_user_id=user, followed_user_id=self_user).save()


class AdjustingScheduleForm(forms.ModelForm):
    class Meta:
        model = AdjustingSchedule
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
            # id = print(args)
            # self.fields[f"friend{i}"].queryset = AdjustingSchedule(id=id)
            # self.fields[f"friend{i}"].queryset = Friend(followed_user_id=)
