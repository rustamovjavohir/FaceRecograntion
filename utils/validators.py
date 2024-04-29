import re

from django.core.exceptions import ValidationError
from datetime import date

from rest_framework import serializers

from apps.auth_user import constants


def phone_validator(value):
    format_text = 'Номер телефона должен быть в формате: 998XXXXXXXXX'
    if not value.isdigit():
        raise ValidationError(f'Номер телефона должен состоять только из цифр.\n{format_text}')
    elif len(value) != 12:
        raise ValidationError(f'Номер телефона должен состоять из 12 цифр.\n{format_text}')
    elif not value.startswith('998'):
        raise ValidationError(f'Номер телефона должен начинаться с (998).\n{format_text}')


def date_of_birth_validator(value):
    if value > date.today():
        raise ValidationError('Дата рождения не может быть больше сегодняшней даты.')
    elif value.year < 1900:
        raise ValidationError('Дата рождения не может быть меньше 1900 года.')


def validate_ids(data, field="external_id", unique=True):
    if isinstance(data, list):
        id_list = [x[field] for x in data]

        if unique and len(id_list) != len(set(id_list)):
            raise ValidationError("Multiple updates to a single {} found".format(field))

        return id_list

    return [data]


def card_number_validator(value):
    format_text = 'Номер карты должен быть в формате: 8600XXXXXXXXXXXX'
    if not value.isdigit():
        raise ValidationError(f'Номер карты должен состоять только из цифр.\n{format_text}')
    elif len(value) != 16:
        raise ValidationError(f'Номер карты должен состоять из 16 цифр.\n{format_text}')


def expire_date_validator(value):
    format_text = 'Срок действия карты должен быть в формате: MMYY'
    if not value.isdigit():
        raise ValidationError(f'Срок действия карты должен состоять только из цифр.\n{format_text}')
    elif len(value) != 4:
        raise ValidationError(f'Срок действия карты должен состоять из 4 цифр.\n{format_text}')


def validate_otp(value, length: int = 4):
    if not value.isdigit():
        raise ValidationError('Код подтверждения должен состоять только из цифр.')
    elif len(value) != length:
        raise ValidationError(f'Код подтверждения должен состоять из {length} цифр.')


def file_size_validator(value):  # add this to some file where you can import it from
    limit = 1024 * 1024
    if value.size > limit:
        raise ValidationError('Файл слишком большой. Размер не должен превышать 1 Мб.')


def password_validator(self, value):
    user = self.context['request'].user
    if len(value) < 8:
        raise serializers.ValidationError(constants.PASSWORD_MUST_CONTAIN_AT_LEAST_8_CHARACTERS)
    if not re.search(r'\d', value):
        raise serializers.ValidationError(constants.PASSWORD_MUST_CONTAIN_AT_LEAST_ONE_NUMBER)
    if not re.search(r'[A-Z]', value):
        raise serializers.ValidationError(constants.PASSWORD_MUST_CONTAIN_AT_LEAST_ONE_CAPITAL_LETTER)
    if user.username in value:
        raise serializers.ValidationError(constants.PASSWORD_MUST_NOT_CONTAIN_LOGIN)
    return value
