from django.db import models
from django.core.validators import RegexValidator
from persiantools import digits


class GeneralFile(models.Model):

    first_name = models.CharField(
        max_length=50,
        verbose_name="نام"
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name="نام خانوادگی"
    )

    national_code = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="کد ملی",
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="کد ملی باید دقیقاً ۱۰ رقم باشد."
            )
        ]
    )

    phone_number = models.CharField(
        max_length=11,
        blank=True,
        verbose_name="شماره همراه",
        validators=[
            RegexValidator(
                regex=r'^09\d{9}$',
                message="شماره همراه باید با 09 شروع شود و 11 رقم باشد."
            )
        ]
    )

    file_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="شماره پرونده"
    )

    def save(self, *args, **kwargs):
        # Normalize Persian/Arabic digits → English digits
        if self.national_code:
            self.national_code = digits.fa_to_en(self.national_code)

        if self.phone_number:
            self.phone_number = digits.fa_to_en(self.phone_number)

        if self.file_number:
            self.file_number = digits.fa_to_en(self.file_number)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.file_number}"