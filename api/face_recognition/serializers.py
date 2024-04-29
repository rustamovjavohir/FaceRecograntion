from rest_framework import serializers


class TrainFaceSerializer(serializers.Serializer):
    image_list = serializers.ListField(required=True)
    user_id = serializers.CharField(required=True)
