from django.urls import path

from api.face_recognition.views import (FaceTrainView, FaceListView, TestView, FaceRecognizeView, FaceDetectionView,
                                        FaceDeleteView)

urlpatterns = [
    path('train/', FaceTrainView.as_view()),
    path('recognize/', FaceRecognizeView.as_view()),
    path('list/', FaceListView.as_view()),
    path('delete/', FaceDeleteView.as_view()),
    path('detection/', FaceDetectionView.as_view()),
    path('test/', TestView.as_view()),
]
