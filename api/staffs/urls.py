from django.urls import path

from api.staffs.views import (StaffCreateView, )

urlpatterns = [
    path('create/', StaffCreateView.as_view()),
]
