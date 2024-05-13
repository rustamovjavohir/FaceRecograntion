from django.urls import path, include

from api.face_recognition import urls as face_recognition_urls
from api.staffs import urls as staffs_urls

urlpatterns = [
    path("face/", include(face_recognition_urls)),
    path("staffs/", include(staffs_urls)),
]
