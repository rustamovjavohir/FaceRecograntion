import requests
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# from utils.responses import Response
from rest_framework.response import Response
from services.face_recognition import FaceRecognitionService
from api.face_recognition.serializers import (TrainFaceSerializer, FaceRecognizeSerializer, DeleteFaceSerializer,
                                              FaceDetectionSerializer)


class FaceTrainView(APIView):
    service = FaceRecognitionService()

    def post(self, request):
        serializer = TrainFaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image_list = serializer.validated_data.get('image_list')
        user_id = serializer.validated_data.get('user_id')
        response = self.service.train_face(image_list, user_id)
        return Response(data=response)


class FaceListView(APIView):
    service = FaceRecognitionService()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        response = self.service.face_list()
        return Response(data=response)


class FaceRecognizeView(APIView):
    service = FaceRecognitionService()

    def post(self, request):
        serializer = FaceRecognizeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image_data = serializer.validated_data.get('image')
        response = self.service.recognize_face(image_data)
        return Response(data=response)


class FaceDeleteView(APIView):
    service = FaceRecognitionService()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = DeleteFaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.validated_data.get('user_id')
        response = self.service.delete_face(user_id)
        return Response(data=response)


class FaceDetectionView(APIView):
    service = FaceRecognitionService()

    def post(self, request):
        serializer = FaceDetectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image_data = serializer.validated_data.get('image')
        response = self.service.face_detection(image_data)
        return Response(data=response)


class CheckFaceView(APIView):
    service = FaceRecognitionService()

    def post(self, request):
        serializer = FaceRecognizeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image_data = serializer.validated_data.get('image')
        response = self.service.face_detection_and_recognize(image_data)
        return Response(data=response)


class TestView(APIView):
    def post(self, request):
        url = "http://localhost:8008/v1/vision/face/register"
        image_data = open("image_1.jpg", "rb").read()
        files = {"image": image_data}
        response = requests.post(url, files=files, data={"userid": "test"}).json()
        return Response(data=response)
