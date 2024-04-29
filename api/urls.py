from django.urls import path

from api.face_recognition.views import FaceRecognitionView, FaceRecognitionListView

urlpatterns = [
    path('face/recognize/', FaceRecognitionView.as_view()),
    path('face/list/', FaceRecognitionListView.as_view()),
]
