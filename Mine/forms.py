from django import forms

from .models import Madan


class MadanForm(forms.ModelForm):
    class Meta:
        model = Madan
        fields = (
            'name',
            'stone_type',
            'shomareh_mojavez_kashf',
            'shomareh_parvaneh_bahrevardari',
            'tonazh_bahrebardari',
            'payment',
            'province',
            'city',
            'village',
            'location_url',
            'description',
        )
        labels = {
            'name': "نام معدن",
            'stone_type': "نوع سنگ",
            'shomareh_mojavez_kashf': "شماره پروانه کشف",
            'shomareh_parvaneh_bahrevardari': "شماره پروانه بهره برداری",
            'tonazh_bahrebardari': " حداق تناژ تقریبی",
            'payment': "حقوق دولتی",
            'province': "استان",
            'city': "شهر",
            'village': "روستا",
            'location_url': "لینک لوکیشن",
            'description': "توضیحات",
        }
