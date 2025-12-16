from django import forms
from .models import GeneralFile
from persiantools import digits

class GeneralFileForm(forms.ModelForm):
    class Meta:
        model = GeneralFile
        fields = [
            "first_name",
            "last_name",
            "national_code",
            "phone_number",
            "file_number",
        ]
    def clean_national_code(self):
        value = self.cleaned_data.get("national_code")
        if value:
            value = digits.fa_to_en(value)
        return value

    def clean_phone_number(self):
        value = self.cleaned_data.get("phone_number")
        if value:
            value = digits.fa_to_en(value)
        return value

    def clean_file_number(self):
        value = self.cleaned_data.get("file_number")
        if value:
            value = digits.fa_to_en(value)
        return value