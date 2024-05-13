from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from utils.models import BaseModel


class User(AbstractUser):
    profile_photo = models.ImageField(upload_to='user/profile_photos',
                                      null=True, blank=True,
                                      verbose_name='Фото профиля',
                                      default='user/profile_photos/default.png')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    objects = UserManager()


class Staff(BaseModel):
    full_name = models.CharField(max_length=255,
                                 verbose_name='ФИО')
    department = models.CharField(max_length=255,
                                  null=True, blank=True,
                                  verbose_name='Отдел')
    telegram_id = models.BigIntegerField(unique=True,
                                         verbose_name='Telegram ID')

    def __str__(self):
        return self.full_name

    class Meta:
        indexes = [
            models.Index(fields=['telegram_id'])
        ]
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
