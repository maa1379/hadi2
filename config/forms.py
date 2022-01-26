from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.Textarea()

