from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator


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
        validators=[
            RegexValidator(r'^\d{10}$', "کد ملی باید دقیقاً ۱۰ رقم باشد.")
        ],
        unique=True,
        verbose_name="کد ملی"
    )

    phone_number = models.CharField(
        max_length=11,
        validators=[
            RegexValidator(r'^09\d{9}$', "شماره همراه باید با 09 شروع شود و 11 رقم باشد.")
        ],
        unique=True,
        verbose_name="شماره همراه"
    )

    file_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="شماره پرونده"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.file_number}"