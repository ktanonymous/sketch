from django import forms


class FriendApplicationForm(forms.Form):
    email1 = forms.EmailField(
        max_length=255,
        label='Email1',
    )
    email2 = forms.EmailField(
        max_length=255,
        label='Email2',
        required=False
    )
    email3 = forms.EmailField(
        max_length=255,
        label='Email3',
        required=False
    )
    email4 = forms.EmailField(
        max_length=255,
        label='Email4',
        required=False
    )
    email5 = forms.EmailField(
        max_length=255,
        label='Email5',
        required=False
    )

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
