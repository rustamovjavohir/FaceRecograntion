from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from api.staffs.serializers import StaffSerializer
from apps.auth_user.models import Staff


class StaffCreateView(CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


