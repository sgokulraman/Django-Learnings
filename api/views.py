from rest_framework.viewsets import ModelViewSet
from .models import Student_details
from .serializers import Student_Serializers
class Api_router(ModelViewSet):
    queryset = Student_details.objects.all()
    serializer_class = Student_Serializers