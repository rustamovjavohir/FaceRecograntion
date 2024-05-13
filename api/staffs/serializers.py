from apps.auth_user.models import Staff
from rest_framework import serializers


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (
            'id',
            'full_name',
            'department',
            'telegram_id',
        )
