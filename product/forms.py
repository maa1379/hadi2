from django import forms



class UploadForm(forms.Form):
    file=forms.FileField()


class EmailForm(forms.Form):
    subject=forms.CharField(max_length=255)
    message=forms.Textarea()

