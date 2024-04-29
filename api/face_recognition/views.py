from rest_framework.views import APIView
from utils.responses import Response
from services.face_recognition import FaceRecognitionService
from api.face_recognition.serializers import TrainFaceSerializer


class FaceRecognitionView(APIView):
    service = FaceRecognitionService()

    def post(self, request):
        serializer = TrainFaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image_list = serializer.validated_data.get('image_list')
        user_id = serializer.validated_data.get('user_id')
        response = self.service.train_face(image_list, user_id)
        return Response(data=response, message='success')


class FaceRecognitionListView(APIView):
    service = FaceRecognitionService()

    def get(self, request):
        response = self.service.face_list()
        return Response(data=response, message='success')
