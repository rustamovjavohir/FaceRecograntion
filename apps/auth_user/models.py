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
