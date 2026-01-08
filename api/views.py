from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
class Student_view(ModelViewSet):
    
    queryset = Student_details.objects.all()
    serializer_class = Student_serializers
    
    
class Student_problem_view(ModelViewSet):
    queryset = Student_problems.objects.all()
    serializer_class = Student_Problem_Serializers
    
    
class Leader_View(ModelViewSet):
    queryset = Leader_login.objects.all()
    serializer_class = Leader_Access_serializer