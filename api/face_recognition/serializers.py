from rest_framework import serializers


class TrainFaceSerializer(serializers.Serializer):
    image_list = serializers.ListField(required=True)
    user_id = serializers.CharField(required=True)


class FaceRecognizeSerializer(serializers.Serializer):
    image = serializers.CharField(required=True)


class DeleteFaceSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)


class FaceDetectionSerializer(serializers.Serializer):
    image = serializers.CharField(required=True)
