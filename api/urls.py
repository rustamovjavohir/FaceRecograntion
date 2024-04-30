from django.urls import path, include

from api.face_recognition import urls as face_recognition_urls

urlpatterns = [
    path("", include(face_recognition_urls)),
]
