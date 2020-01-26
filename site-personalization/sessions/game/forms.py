from django import forms
from .models import Game


class CreateForm(forms.ModelForm):
    # text = forms.CharField(widget=forms.Textarea, label='Отзыв')
    # def __init__(self, *args, **kwargs):
    #     super(RegistrationFormTOS, self).__init__(*args, **kwargs)
    #     self.fields['email'].label = "New Email Label"

    class Meta(object):
        model = Game
        fields = ('key_min', 'key_max', 'key')


class InputForm(forms.Form):
    key = forms.IntegerField(label='Ваш вариант')
