from django import forms


class Forms(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False, label='your Email')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('not enough words.')
        return message