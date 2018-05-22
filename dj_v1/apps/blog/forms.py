from django import forms


class WriteForm(forms.Form):
    title = forms.CharField(max_length=20, required=True)
    author = forms.CharField(max_length=20, required=True)
    content = forms.CharField(widget=forms.Textarea)


class MessageForm(forms.Form):
    message = forms.CharField(max_length=500, required=True)