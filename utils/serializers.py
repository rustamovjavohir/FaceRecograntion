from rest_framework import serializers


class FilteredActiveListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(is_active=True)
        return super(FilteredActiveListSerializer, self).to_representation(data)
