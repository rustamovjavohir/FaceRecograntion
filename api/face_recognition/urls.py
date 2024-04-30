from django.urls import path

from api.face_recognition.views import (FaceTrainView, FaceListView, TestView, FaceRecognizeView, FaceDetectionView,
                                        FaceDeleteView)

urlpatterns = [
    path('face/train/', FaceTrainView.as_view()),
    path('face/recognize/', FaceRecognizeView.as_view()),
    path('face/list/', FaceListView.as_view()),
    path('face/delete/', FaceDeleteView.as_view()),
    path('face/detection/', FaceDetectionView.as_view()),
    path('face/test/', TestView.as_view()),
]
