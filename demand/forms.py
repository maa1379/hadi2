from django import forms

from .models import Hold, Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model=Visit
        fields=("")
