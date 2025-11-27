from django import forms
from .models import GeneralFile


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
